import pandas as pd

class Solution():
    def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
        ans = sorted(employee["salary"].unique(), reverse=True)[N-1:N]
        if (N > employee["salary"].nunique() or N <= 0) :
            return pd.DataFrame(data={f"getNthHighestSalary({N})" : None}, index=[" "])
        else:
            return pd.DataFrame(data={f"getNthHighestSalary({N})" : ans})