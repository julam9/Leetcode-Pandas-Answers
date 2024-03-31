import pandas as pd

data={"col1" : [[], [1,2,3], [], [4,5], []]}
df=pd.DataFrame(data)

# check if each element in the column is an empty list
empty_list_indices = df["col1"].apply(lambda x:isinstance(x, list) and len(x)==0)

# print the indices of rows contining empty lists
#print(empty_list_indices[empty_list_indices== True].index.tolist())
print(empty_list_indices)