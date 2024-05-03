import pandas as pd

class Solution:
    def exchange_seats(seat:pd.DataFrame) -> pd.DataFrame:
        if len(seat)%2 == 0:
            seat["new_id"] = seat["id"]-1 if seat%2==0 else seat["id"]+1
        else:
            seat[0:len(seat)]["new_id"]  