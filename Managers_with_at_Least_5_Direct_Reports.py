import pandas as pd

class Solution():
    def find_managers(employee:pd.DataFrame) -> pd.DataFrame:
        manager_data = pd.merge(employee, employee, left_on = "managerId", right_on="id", right_suffix="_y").rename(columns={"name_y" : "manager_name"})
        return manager_data["manager_name"].value_counts().reset_index().query(" count > 4").drop()