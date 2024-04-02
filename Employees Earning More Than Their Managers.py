import pandas as pd

def find_employees(employees:pd.DataFrame) -> pd.DataFrame:
    e2 = pd.merge(employees, employees, left_on="managerId", right_on="id", how="left", suffixes=["1", "2"])
    return e2 [e2["salary1"] > e2["salary2"]]["name1"]

aa=pd.DataFrame(data={"id":[1,2,3,4], "name" : ["A", "B", "C", "D"], "salary":[7000,8000,6000,9000], "managerId":[3,4,"Null","Null"]})
print(find_employees(aa)) 