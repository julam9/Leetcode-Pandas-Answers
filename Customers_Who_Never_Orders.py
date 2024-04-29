import pandas as pd

class Solution:
    def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
        
        # join the customers and orders table using left join 
        d2 = pd.merge(customers, orders, how="left", left_on="id", right_on="customerId")
        
        # return the row where the id from order table is null (alternatively, you can use the customerId from order table to checking the null row)
        return d2[d2["id_y"].isnull()].iloc[:, 1:2].rename(columns = {"name" : "Customers"})