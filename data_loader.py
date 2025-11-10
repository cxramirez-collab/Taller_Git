import pandas as pd

def load_data(path="./data/students.csv"):
  df = pd.read_csv(path)
  print(f"Loaded {len(df)} student records.")
  return df
