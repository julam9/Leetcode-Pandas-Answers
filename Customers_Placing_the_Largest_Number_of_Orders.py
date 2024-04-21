import pandas as pd

class Solution():
    def largest_orders(orders:pd.DataFrame) -> pd.DataFrame:
        cust_order_count = orders["customer_number"].value_counts().reset_index()