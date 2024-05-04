import pandas as pd

class Solution:
    def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
        triangle["triangle"] = "Yes" if sum([triangle.x + triangle.y > triangle.z, triangle.x + triangle.z > triangle.y, triangle.y + triangle.z > triangle.x]) == 3 else "No"
        return triangle 