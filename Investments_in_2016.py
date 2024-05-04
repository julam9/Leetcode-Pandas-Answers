import pandas as pd

class Solution:
    def find_investments(insurance:pd.DataFrame) -> pd.DataFrame:
        rule1_pid = insurance.groupby("pid")["inv_2015"].count()
        return rule1_pid