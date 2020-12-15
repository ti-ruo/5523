import sys
import pandas as pd
f = open("stocks/covid_old.csv", "r")
#Date	Total Cases	New Cases	7-Day Moving Avg	Rate per 100000
'''
df = pd.DataFrame(columns=['A'])
for i in range(5):
    df = df.append({'A': i}, ignore_index=True)
'''
df = pd.DataFrame(columns=['Date','Total','New','7Day','per10000'])
#print(df.info)
for lines in f:
    lines = lines.strip("\n")
    lines = lines.split(",")
    dates = lines[0].split(" ")
    if int(dates[1])<10:
        dates[1] = "0"+dates[1]
    if dates[0] == "Jan":
        ndates = dates[2]+"01"+dates[1]
        #print(ndates)
    if dates[0] == "Feb":
        ndates = dates[2]+"02"+dates[1]
        #print(ndates)
    if dates[0] == "Mar":
        ndates = dates[2]+"03"+dates[1]
        #print(ndates)
    if dates[0] == "Apr":
        ndates = dates[2]+"04"+dates[1]
        #print(ndates)
    if dates[0] == "May":
        ndates = dates[2]+"05"+dates[1]
        #print(ndates)
    if dates[0] == "Jun":
        ndates = dates[2]+"06"+dates[1]
        #print(ndates)
    if dates[0] == "Jul":
        ndates = dates[2]+"07"+dates[1]
        #print(ndates)
    if dates[0] == "Aug":
        ndates = dates[2]+"08"+dates[1]
        #print(ndates)
    if dates[0] == "Sep":
        ndates = dates[2]+"09"+dates[1]
        #print(ndates)
    if dates[0] == "Oct":
        ndates = dates[2]+"10"+dates[1]
    if dates[0] == "Nov":
        ndates = dates[2]+"11"+dates[1]
    if dates[0] == "Dec":
        ndates = dates[2]+"12"+dates[1]
    df = df.append({'Date': ndates,'Total':lines[1],'New':lines[2],'7Day':lines[3],'per10000':lines[4]}, ignore_index=True)
#print(df)
addr = "stocks/new_covid.csv"
df.to_csv(addr,index=False)