#!/usr/bin/env python3
import os
import json
from datetime import datetime

def process_data():
  """Simulate processing some data and return results"""
  # In a real scenario, this might read from an API or file.
  data = {
          "processed_at": datetime.now().isoformat(),
          "values": [10,20,30,40,50],
          "average": 30,
          "sum": 150

      }
  return data

def save_results(data, output_file="results/output.json"):
    """Save the processed data to a JSON file"""
    #Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file),exist_ok=True)

    #Write date to the file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Results saved to {output_file}")
    return True

def main():
    print("Starting data processing script...")
    data = process_data()
    success = save_results(data)
    if success:
        print("Processing completed successfully!")
    else:
        print("Error occurred during processing")
        return 1
    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
