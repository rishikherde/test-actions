import pandas as pd
import sys

csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

def is_uppercase(value):
    return isinstance(value, str) and value == value.upper()

all_uppercase = all(df[col].map(is_uppercase).all() for col in df.select_dtypes(include=['object']).columns)

if all_uppercase:
    print("All string columns are uppercase")
    with open("test_report.txt","w") as f:
        f.write("test passed! \n")
    exit(0)
else:
    print("Test failed: Some string columns are not uppercase")
    with open("test_report.txt", "w") as f:
        f.write("Test failed!\n")
    exit(1)