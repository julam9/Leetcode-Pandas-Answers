import pandas as pd 

class Solution():
    def find_customer_refree(customer:pd.DataFrame) -> pd.DataFrame:
        return customer.query("referee_id != 2 | referee_id.isnull()")["name"].to_frame()