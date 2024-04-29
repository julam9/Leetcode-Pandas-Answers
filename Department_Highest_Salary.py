import pandas as pd

class Solution:
    def department_highest_salary(employee:pd.DataFrame, department:pd.DataFrame) -> pd.DataFrame:
        return employee.groupby(["departmend_id", "salary"], as_index=False)[["name", "salary", "departmentId"]].agg("max")