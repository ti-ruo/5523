# to calcluate the rate
# Crisis Return Cal:  (Price at 3/31/2020  /  price at 12/31/2019) - 1
# Post Crisis Return Cal: Price at 11/11/2020 / Price at 3/31/2020) - 1 
# get the sector name and the top 11 result of the table
import sys
import pandas as pd
import csv
file_f = open("stocks/etf_total.csv", "r")
res = dict()
skip = 0
for lines in file_f:
    if skip == 0:
        skip = 1
    else:
        lines = lines.strip("\n").split(",")
        ticker = lines[2]
        if ticker in res.keys():
            temp = res.values()
            ret_val = (float(lines[0])/float(res[ticker]))-1
            res[ticker] = ret_val
        else:
            res[ticker] = float(lines[0])
print(res)

csv_file = "stocks/etf_return_total_crisis.csv"
with open(csv_file, 'w') as f:
    for key in res.keys():
        f.write("%s,%s\n"%(key,res[key]))