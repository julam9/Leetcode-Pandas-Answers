import pandas as pd

class Solution:
    def sales_person(sales_person:pd.Dataframe, company:pd.DataFrame, orders:pd.DataFrame) -> pd.DataFrame:
        sales_order = pd.merge(sales_person, orders, how='left', on='sales_id') 
        full_table = pd.merge(sales_order, company, how='inner', on='com_id')