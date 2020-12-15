import pandas as pd
df = pd.read_csv("evaled.csv")
df = df[df.Type == "Stock"]
df = df.fillna(0)
df.to_csv("modified.csv",index = False)