import pandas as pd

class Solution():
    def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
        ranking_salaries = employee.rank()