import pandas as pd
df = pd.read_csv("stocks/new_covid.csv")
df2 = pd.read_csv("stocks/SampleData.csv")
#inner_merged_total = pd.merge(climate_temp, climate_precip, on=["STATION", "DATE"])
merge = pd.merge(df,df2,how="right",on=["Date"])
addr = "stocks/merged.csv"
merge.to_csv(addr,index=False)