import pandas as pd

class Solution():   
    def order_scores(scores: pd.DataFrame) -> pd.DataFrame :
        
        # ordering the scores from the highest to the lowest
        d2 = scores.sort_values(by="score", ascending=False)
        
        # giving rank to the ordered scores and change the deafult output of rank from float to integer 
        d2["rank"] = d2["score"].rank(method="dense", ascending=False).astype("int")
        
        # return the rank
        return d2.iloc[:, 1:]