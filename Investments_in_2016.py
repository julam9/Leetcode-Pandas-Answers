import pandas as pd

class Solution():
    def find_investments(insurance:pd.DataFrame) -> pd.DataFrame:
        rule1_pid = insurance[insurance["tiv_2015"]]
        rule2_pid = insurance