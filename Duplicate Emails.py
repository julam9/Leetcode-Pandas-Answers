import pandas as pd 

def duplicate_emails(person:pd.DataFrame) -> pd.DataFrame:
    return person["email"].value_counts().reset_index()