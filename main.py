from data_loader import load_data
from analysis import dropout_summary

if __name__ == "__main__":
  data = load_data()
  rate, cause = dropout_summary(data)
  print(f"Dropout rate: {rate}%")
  print(f"Most common dropout cause:{cause}")