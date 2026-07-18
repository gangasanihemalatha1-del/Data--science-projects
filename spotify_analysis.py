import pandas as pd
ur 1 ="https://githubusercontent.com"
df=pd.read_csv(ur1)
print("spotify Data successfully loaded!")
print(f"The dataset contains {df.shape[0]}songs and {df.shape[1]}columns.")
