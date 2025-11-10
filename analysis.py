def dropout_rate(df):
  total = len(df)
  dropped = len(df[df["status"] == "Dropped"])
  rate = dropped / total * 100
  return round(rate, 2)
