def dropout_rate(df):
  total = len(df)
  dropped = len(df[df["status"] == "Dropped"])
  rate = dropped / total * 100
  return round(rate, 2)

def most_common_dropout_cause(df):
  dropped_df = df[df["status"] == "Dropped"]
  if "cause" not in df.columns:
    return None
  if dropped_df["cause"].dropna().empty:
    return None
  most_common_dropout_cause = dropped_df["cause"].value_counts().idxmax()
  return most_common_dropout_cause

def dropout_summary(df):
  rate = dropout_rate(df)
  cause = most_common_dropout_cause(df)
  return rate, cause