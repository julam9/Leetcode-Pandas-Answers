import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    '''
    select only email with concurences equal to 1
    '''
    
    return pd.DataFrame(data={"email" : person["email"].value_counts().reset_index().query("count > 1").iloc[:, 0]})
