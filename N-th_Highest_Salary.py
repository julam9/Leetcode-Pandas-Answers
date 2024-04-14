import pandas as pd

class Solution():
    def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
        
        # sorting the salary from the highest to lowest. After that, select the N-th highest 
        ans = sorted(employee["salary"].unique(), reverse=True)[N-1:N]
        
        # checking if the N is greater than count of unique salary or the N is less than or equal zero
        if (N > employee["salary"].nunique() or N <= 0) :
            
            # if yes, then return null (None) because N can't be more than count of unique salary or N must be start from 1
            return pd.DataFrame(data={f"getNthHighestSalary({N})" : None}, index=[" "])
        else:
            
            # if no, return the N-th highest salary
            return pd.DataFrame(data={f"getNthHighestSalary({N})" : ans})