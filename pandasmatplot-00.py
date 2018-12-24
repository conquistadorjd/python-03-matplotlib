import pandas as pd
import numpy as np
import psycopg2
from matplotlib import pyplot as plt



################################################################################################### getting data ready
fromDate 	= '2017-12-01'
toDate		= '2018-01-31'
symbol 		=  'KOTAKBANK'

conn = psycopg2.connect(database='equityindia', user="admin", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("SELECT  symbol, date, prevclose, open, high, low, close, vwap, volume,turnover,deliverableqty, percentdelivery from NSEEQUITYDATA WHERE date > %s and date <= %s and SYMBOL =%s ORDER BY DATE ASC",(fromDate, toDate,symbol,))
rows = cur.fetchall()
df = pd.DataFrame(rows,columns=['symbol', 'date','prevclose', 'open','high','low', 'close','vwap','volume','turnover','deliverableqty','percentdelivery'])
df2 = df[['date', 'close']].copy()
df2['date'] = pd.to_datetime(df2['date'])
df2['close'] = df2['close'].astype(np.float64)

#print(df2.dtypes)
print(df2)
#print('Columns :', len(df2.columns))

df2.index = df2['date']
del df2['date']
print('**** After change',df2)
df2.plot()
plt.show()
################################################################################################### getting data ready
#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#print(ts)
#ts = ts.cumsum()
#ts.plot()

# plt.show()


################################################################################################### getting data ready
#ts = pd.Series(df2[['close']], df2[['date']])
#print(df2[['close']])
#ts = ts.cumsum()
#ts.plot()

#plt.show()