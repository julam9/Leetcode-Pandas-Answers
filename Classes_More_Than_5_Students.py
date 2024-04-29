import pandas as pd

class Solution:
    def find_classes(courses:pd.DataFrame) -> pd.DataFrame:
        student_course_count = courses["student"].value_counts().reset_index()
        return student_course_count.query("count > 1")