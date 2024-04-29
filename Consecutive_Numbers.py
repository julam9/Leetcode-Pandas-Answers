import pandas as pd

class Solution:
    def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
        
        # inserting a new variable where it is the first element after (first lag of) the current element of orig column
        logs["num2"] = logs["num"].shift(periods=1)
        
        # inserting a new variable where it is the second element after (second lag of) the current element of orig column
        logs["ConsecutiveNums"] = logs["num2"].shift(periods=1)
        
        # return row where the orig, first lag, second lag have the same value
        return logs[(logs["num"] == logs["num2"]) & (logs["num2"] == logs["ConsecutiveNums"])].iloc[:, 3:]