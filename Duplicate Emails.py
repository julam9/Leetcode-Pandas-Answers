import pandas as pd 

class Solution():
    def duplicate_emails(person:pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame(data={"email" : person["email"].value_counts().reset_index().query("count > 1").iloc[:, 0]})
