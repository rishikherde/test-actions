import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.upper()

df.to_csv(output_file, index=False)