import pandas as pd 

def duplicate_emails(person:pd.DataFrame) -> pd.DataFrame:
    return person["email"].value_counts().reset_index().query("count > 1")

#A = pd.DataFrame(data={"A" : [1,1,1,2,2,3,3,5,0]})
#print(A.value_counts().reset_index().query("count > 1"))
