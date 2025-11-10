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

def dropout_by_career(df):
    if "career" not in df.columns:
        return {}
    results = {}
    careers = df["career"].unique()
    for career in careers:
        subset = df[df["career"] == career]
        total = len(subset)
        dropped = len(subset[subset["status"] == "Dropped"])
        if total > 0:
            rate = round((dropped / total) * 100,2)
            results[career] = rate
    return results
