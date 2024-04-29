import pandas as pd

class Solution:
    def delete_duplicate_emails(person: pd.DataFrame) -> None:
        '''
        using the drop_duplicates function from pandas module
        '''
        person.sort_values(by="id").drop_duplicates(subset=["email"], inplace=True)