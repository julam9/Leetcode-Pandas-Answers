import pandas as pd

class Solution:
    def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
        num_freq = my_numbers.value_counts().reset_index()
        single_freq = num_freq.query("count == 1")
        return max(single_freq["num"])