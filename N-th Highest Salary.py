import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if employee["salary"].nunique() > N:
        salary_Nth = employee.sort_values(by="salary", ascending=False)[N]
        return pd.DataFrame(data={f"getNthHighestSalary({N})" : employee.sort_values(by="salary", ascending=False)}) 
    else:
        return pd.DataFrame(data={f"getNthHighestSalary{N}" : None}, index=" ")