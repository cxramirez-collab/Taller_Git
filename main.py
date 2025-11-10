rom data_loader import load_data
from analysis import dropout_rate

if __name__ == "__main__":
  data = load_data()
  rate = dropout_rate(data)
  print(f"Dropout rate: {rate}%")
