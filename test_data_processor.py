import unittest
import os
import json
from data_processor import process_data, save_results

class TestDataProcessor(unittest.TestCase):

    def test_process_data(self):
      """Test that process_data returns a dictionary with expected keys."""
      result = process_data()
      self.assertIsInstance(result, dict)
      self.assertIn('processed_at', result)
      self.assertIn('values', result)
      self.assertIn('average', result)
      self.assertIn('sum', result)

    def test_save_results(self):
      """Test that save_results correctly saves data to a file."""
      test_data = {"test": "data"}
      test_file = "results/test_output.json"

      # Save the test data
      save_results(test_data, test_file)

      # Check if file exists and contains correct data
      self.assertTrue(os.path.exists(test_file))
      with open(test_file, 'r') as f:
        saved_data = json.load(f)

      self.assertEqual(saved_data, test_data)

if __name__ == '__main__':
    unittest.main()
