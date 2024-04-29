import pandas as pd

class Solution:
    def human_traffic(stadium:pd.DataFrame) -> pd.DataFrame:
        return stadium.query("people > 100")