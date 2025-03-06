import pandas as pd
import sys
import os

input_file = sys.argv[1]

df = pd.read_csv(input_file)

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.upper()

output_file = os.path.join("data", "transformed.csv")
df.to_csv(output_file, index=False)
print(f"File created at: {output_file}")
