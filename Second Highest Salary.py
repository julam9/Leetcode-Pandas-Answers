import pandas as pd

class Solution():
    def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
        if employee["salary"].nunique() > 1:
            return pd.DataFrame(data = {"SecondHighestSalary" : employee[employee["salary"] < employee["salary"].max()].sort_values(by="salary", ascending=False)["salary"].head(1)})
        else:
            return pd.DataFrame(data = {"SecondHighestSalary" : None}, index=[" "]) 