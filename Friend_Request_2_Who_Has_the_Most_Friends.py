import pandas as pd

class Solution:
    def most_friends(request_accepted:pd.DataFrame) -> pd.DataFrame:
        request_n = request_accepted["requester_id"].value_counts().reset_index()