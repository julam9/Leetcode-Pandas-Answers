import pandas as pd

class Solution():
    def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
        salaries_data = employee.merge(department, how="inner", left_on="departmentId", right_on = "id", suffixes=["", "_y"]).rename(columns={"name" : "Employee", "name_y" : "Department", "salary" : "Salary"}).drop(columns=["id", "id_y", "departmentId"])
        salaries_data["salary_rank"] = salaries_data.groupby("Department")["Salary"].rank(method="dense", ascending=False)
        return salaries_data.query("salary_rank < 4").loc[:, ["Department", "Employee", "Salary"]]