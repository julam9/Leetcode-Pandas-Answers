import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["next1element"] = logs.loc[1, 1:]
    logs["next2element"] = logs.loc[1, 2:]