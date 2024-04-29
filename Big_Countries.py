import pandas as pd

class Solution:
    def big_countries(world:pd.DataFrame) -> pd.DataFrame:
        return world.query("area >= 3000000 | population >= 25000000")