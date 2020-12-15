import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
df=pd.read_html(url, header=0)[0]
df.head()
df.to_csv(r'Desktop/500.csv')