import pandas as pd


class Solution :
    def find_employees(employees:pd.DataFrame) -> pd.DataFrame:
        e2 = pd.merge(employees, employees, left_on="managerId", right_on="id", how="left", suffixes=["1", "2"])
        return e2 [e2["salary1"] > e2["salary2"]]["name1"]