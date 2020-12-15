import yfinance as yf
from datetime import date
#https://pypi.org/project/yfinance/
#https://algotrading101.com/learn/yfinance-guide/
import sys
import pandas as pd
'''
Crisis period: 12/31/2019 to 3/31/2020
Post crisis period: 3/31/2020 to 11/11/2020
'''
file_f = open("etf.csv", "r") # open the cleaned Sp500 list, note all in here are uppercase
'''
addr = "stocks/etf_pre.csv"
output_file =  pd.DataFrame()
for lines in file_f: #str
    try: # use close price
        lines = lines.strip("\n")
        stock = yf.Ticker(lines)
        pd1 = stock.history(start="2019-12-31",end = "2020-01-01", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd2 = {"Date":str(pd1.index[0]).split(' ')[0], "Ticker":lines, "Close":pd1["Close"][0]}
        output_file = output_file.append(pd2,ignore_index=True)
        pd3 = stock.history(start="2020-03-31",end = "2020-04-01", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd4 = {"Date":str(pd3.index[0]).split(' ')[0], "Ticker":lines, "Close":pd3["Close"][0]}
        output_file = output_file.append(pd4,ignore_index=True)
    except Exception as e:
        print("missing: "+str(lines))
        print(e)
output_file.to_csv(addr,index=False)
'''
print("---------------------------------------------------------------")
'''
addr = "stocks/etf_post.csv"
output_file1 =  pd.DataFrame()
for lines in file_f: #str
    try: # use close price
        lines = lines.strip("\n")
        stock = yf.Ticker(lines)
        pd1 = stock.history(start="2020-03-31",end = "2020-04-01", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd2 = {"Date":str(pd1.index[0]).split(' ')[0], "Ticker":lines, "Close":pd1["Close"][0]}
        output_file1 = output_file1.append(pd2,ignore_index=True)
        pd3 = stock.history(start="2020-11-11",end = "2020-11-12", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd4 = {"Date":str(pd3.index[0]).split(' ')[0], "Ticker":lines, "Close":pd3["Close"][0]}
        output_file1 = output_file1.append(pd4,ignore_index=True)
    except Exception as e:
        print("missing: "+str(lines))
        print(e)
output_file1.to_csv(addr,index=False)
'''
print("---------------------------------------------------------------")

addr = "stocks/etf_total.csv"
output_file2 =  pd.DataFrame()
for lines in file_f: #str
    try: # use close price
        lines = lines.strip("\n")
        stock = yf.Ticker(lines)
        pd1 = stock.history(start="2019-12-31",end = "2020-01-01", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd2 = {"Date":str(pd1.index[0]).split(' ')[0], "Ticker":lines, "Close":pd1["Close"][0]}
        output_file2 = output_file2.append(pd2,ignore_index=True)
        pd3 = stock.history(start="2020-11-11",end = "2020-11-12", actions=False)#start="2019-12-30",end = "2020-04-01"
        pd4 = {"Date":str(pd3.index[0]).split(' ')[0], "Ticker":lines, "Close":pd3["Close"][0]}
        output_file2 = output_file2.append(pd4,ignore_index=True)
    except Exception as e:
        print("missing: "+str(lines))
        print(e)
output_file2.to_csv(addr,index=False)
