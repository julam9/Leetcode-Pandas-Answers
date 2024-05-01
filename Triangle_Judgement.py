import pandas as pd

class Solution:
    def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
        triangle["triangle"] = "Yes" if all([triangle.x + triangle.y > triangle.z, triangle.x + triangle.z > triangle.y, triangle.y + triangle.z > triangle.x]) else "No"
        return triangle 