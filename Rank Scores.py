import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame :
    d2 = scores.sort_values(by="score", ascending=False)
    d2["rank"] = d2["score"].rank(method="dense", ascending=False).astype("int")
    return d2.iloc[:, 1:]