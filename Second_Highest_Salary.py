import pandas as pd

class Solution:
    def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
        
        # checking if the salaries are vary 
        if employee["salary"].nunique() > 1:
            
            #if yes, then select all salaries but the highest salary. After that, return the highest salary from the selected salary
            return pd.DataFrame(data = {"SecondHighestSalary" : employee[employee["salary"] < employee["salary"].max()].sort_values(by="salary", ascending=False)["salary"].head(1)})
        else:
            
            # if no, then return null (None)
            return pd.DataFrame(data = {"SecondHighestSalary" : None}, index=[" "]) 