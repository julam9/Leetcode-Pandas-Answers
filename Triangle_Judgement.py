import pandas as pd

class Solution:
    def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
        triangle["triange"] = "Yes" if triangle.x < triangle.y < triangle.z else "No"