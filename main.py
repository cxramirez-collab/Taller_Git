from data_loader import load_data
from analysis import dropout_summary, dropout_by_career

if __name__ == "__main__":
  data = load_data()
  rate, cause = dropout_summary(data)
  print(f"Dropout rate: {rate}%")
  print(f"Most common dropout cause:{cause}")

  print("\nDropout rate by career:")
  rates_by_career = dropout_by_career(data)
  for career, rate in rates_by_career.items():
      print(f"{career}: {rate}%")