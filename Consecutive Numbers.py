import pandas as pd

class Solution():
    def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
        logs["num2"] = logs["num"].shift(periods=1)
        logs["ConsecutiveNums"] = logs["num2"].shift(periods=1)
        return logs[(logs["num"] == logs["num2"]) & (logs["num2"] == logs["ConsecutiveNums"])].iloc[:, 3:]