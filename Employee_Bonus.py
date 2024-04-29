import pandas as pd

class Solution:
    def employee_bonus(employee:pd.DataFrame, bonus:pd.DataFrame) -> pd.DataFrame:
        bonus_id = bonus.query("bonus < 1000")["empId"]
        return employee[employee["empId"].isin(bonus_id)]