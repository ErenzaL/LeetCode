import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["prev"] = logs["num"].shift(1)
    logs["next"] = logs["num"].shift(-1)

    # Check if num == prev == next
    mask = (logs["num"] == logs["prev"]) & (logs["num"] == logs["next"])

    # Get distinct numbers
    result = logs.loc[mask, "num"].unique()
    return pd.DataFrame({'ConsecutiveNums'  : result})