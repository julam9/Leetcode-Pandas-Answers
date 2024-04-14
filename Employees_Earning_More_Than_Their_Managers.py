import pandas as pd


class Solution :
    def find_employees(employees:pd.DataFrame) -> pd.DataFrame:
        
        # joining the table on the table itself (self join) to get who is every employee manager and their manager salary
        e2 = pd.merge(employees, employees, left_on="managerId", right_on="id", how="left", suffixes=["1", "2"])
        
        # comparing the salary of employee and their manager salary. Return row where employee salary more then manager salary
        return e2 [e2["salary1"] > e2["salary2"]]["name1"]