import pandas as pd

class Solution():
    def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame :
        # sorting by date
        weather = weather.sort_values(by="recordDate")
        
        # capitalize first letter of column name
        weather.columns = weather.columns.str.capitalize()
        
        weather["temp_yesterday"] = weather["Temperature"].shift(periods=1)
        return weather[weather["Temperature"] > weather["temp_yesterday"]].loc[:, ["Id"]]