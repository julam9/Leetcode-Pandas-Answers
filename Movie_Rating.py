import pandas as pd

class Solution:
    def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
        return movie_rating.query(" '2020-02-01' <=  crated_at <= '2020-02-29' ")