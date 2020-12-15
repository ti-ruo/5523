import pandas as pd
f = pd.read_csv("merged.csv")
f = f.fillna(0)
evalu = []
for index in f.index:
    #print(f.iloc[index])
    assig_val = 0
    if int(f.loc[index,'Date'])<=20200311:
        if int(f.loc[index,'New']) <= 154:
            assig_val += 2
        elif 154 <= int(f.loc[index,'New']) <= 6284:
            assig_val += 1
        else:
            assig_val -= 1
    else:
        if int(f.loc[index,'New']) <= 6284:
            assig_val += 2
        elif 6284 <= int(f.loc[index,'New']) <= 8731:
            assig_val += 1
        else:
            assig_val -= 1
    if f.loc[index,'Type'] == 'Stock':
        if f.loc[index,'Sector'] == 'Information Technology':
            assig_val += 5
        elif f.loc[index,'Sector'] == 'Consumer Discretionary':
            assig_val += 4
        elif f.loc[index,'Sector'] == 'Communication Services':
            assig_val += 3
        elif f.loc[index,'Sector'] == 'Materials':
            assig_val += 2
        elif f.loc[index,'Sector'] == 'Health Care':
            assig_val += 1
        elif f.loc[index,'Sector'] == 'Industrials':
            assig_val -= 1
        elif f.loc[index,'Sector'] == 'Utilities':
            assig_val -= 2
        elif f.loc[index,'Sector'] == 'Real Estate':
            assig_val -= 3
        elif f.loc[index,'Sector'] == 'Financials':
            assig_val -= 4
        elif f.loc[index,'Sector'] == 'Energy':
            assig_val -= 5
        else:
            assig_val += 0
    if f.loc[index,'Type'] != 'Stock':
        evalu.append("NULL")
    else:
        evalu.append(int(assig_val))
#    print(assig_val)

f['Eval'] = evalu
addr = "evaled.csv"
f.to_csv(addr,index=False)
'''
XLK Information Technology 5
XLY Consumer Discretionary 4
XLC Communication Services 3
XLB Materials 2
XLV Health Care 1
XLP Consumer Staples 0
XLI Industrials -1
XLU Utilities -2
XLRE Real Estate -3
XLF Financials -4
XLE Energy -5
---------------------------------------------------------------
For cases confirmed, the average cases for crisis period is(before 0311):
154
for post crisis period(after 0311):
8731
for all time average:
6284
So for weighted cases point, divides timestamps:
if time is before 0311, then +1 for between 154,6284, +2 for below 154, anything above 6284 assign -1
after 0311, +1 if below 8731, +2 if below 6284, -1 for anything above 8731,
if no date provided, consider it as after 0311, post crisis period.
'''