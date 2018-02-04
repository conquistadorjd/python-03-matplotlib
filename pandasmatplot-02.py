import pandas as pd
import numpy as np
import psycopg2
from matplotlib import pyplot as plt
################################################################################################################
#
#
# 02 : controling the size of plots
################################################################################################################


################################################################################################### getting data ready
fromDate 	= '2017-07-01'
toDate		= '2018-01-31'
symbol 		=  'DAAWAT'

conn = psycopg2.connect(database='equityindia', user="admin", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("SELECT  symbol, date, prevclose, open, high, low, close, vwap, volume,turnover,deliverableqty, percentdelivery,nooftrades from NSEEQUITYDATA WHERE date > %s and date <= %s and SYMBOL =%s ORDER BY DATE ASC",(fromDate, toDate,symbol,))
rows = cur.fetchall()
df = pd.DataFrame(rows,columns=['symbol', 'date','prevclose', 'open','high','low', 'close','vwap','volume','turnover','deliverableqty','percentdelivery','nooftrades'])

df['SMA5'] = df["close"].rolling(5).mean()
df['SMA10'] = df["close"].rolling(10).mean()
df['SMA20'] = df["close"].rolling(20).mean()
df['SMA50'] = df["close"].rolling(50).mean()
df['SMA100'] = df["close"].rolling(100).mean()
df['SMA200'] = df["close"].rolling(200).mean()
df['percentdeliveryMean'] = df["percentdelivery"].rolling(20).mean()
df['verageTradeSize'] = df["volume"]/df["nooftrades"]
df['verageTradeSizeMean'] =  df["verageTradeSize"].rolling(20).mean()
print(df.dtypes)
#### changing datatypes
df['date'] = pd.to_datetime(df['date'])
df['close'] = df['close'].astype(np.float64)
df['open'] = df['open'].astype(np.float64)
df['volume'] = df['volume'].astype(np.float64)
df['percentdelivery'] = df['percentdelivery'].astype(np.float64)

print(df.dtypes)
################################################################################################### getting data ready
ax = plt.subplot2grid((5, 1), (0, 0))

ax1 = plt.subplot2grid((5, 1), (0, 0), rowspan=2)
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is line plot using matplotlib') 

plt.plot(df['date'].values,df['close'].values,color='green',alpha=1,)
plt.plot(df['date'].values,df['SMA10'].values,color='red',alpha=0.5,)
plt.plot(df['date'].values,df['SMA20'].values,color='red',alpha=0.6,)
plt.plot(df['date'].values,df['SMA50'].values,color='red',alpha=0.7,)
plt.plot(df['date'].values,df['SMA100'].values,color='red',alpha=0.8,)
plt.plot(df['date'].values,df['SMA200'].values,color='red',alpha=0.9,)


ax1 = plt.subplot2grid((5, 1), (2, 0), rowspan=1)
plt.ylabel('Volume')  
plt.plot(df['date'].values,df['volume'].values,color='red',alpha=0.5,)

ax1 = plt.subplot2grid((5, 1), (3, 0), rowspan=1)
plt.ylabel('percentdelivery')  
plt.plot(df['date'].values,df['percentdelivery'].values,color='red',alpha=0.5,)
plt.plot(df['date'].values,df['percentdeliveryMean'].values,color='blue',alpha=0.9,)

ax1 = plt.subplot2grid((5, 1), (4, 0), rowspan=1)
plt.ylabel('verageTradeSize')  
plt.plot(df['date'].values,df['verageTradeSize'].values,color='red',alpha=0.5,)
plt.plot(df['date'].values,df['verageTradeSizeMean'].values,color='blue',alpha=0.9,)
plt.show()