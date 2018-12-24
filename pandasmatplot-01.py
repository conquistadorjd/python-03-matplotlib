import pandas as pd
import numpy as np
import psycopg2
from matplotlib import pyplot as plt



################################################################################################### getting data ready
fromDate 	= '2017-01-01'
toDate		= '2018-01-31'
symbol 		=  'APEX'

conn = psycopg2.connect(database='equityindia', user="admin", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("SELECT  symbol, date, prevclose, open, high, low, close, vwap, volume,turnover,deliverableqty, percentdelivery from NSEEQUITYDATA WHERE date > %s and date <= %s and SYMBOL =%s ORDER BY DATE ASC",(fromDate, toDate,symbol,))
rows = cur.fetchall()
df = pd.DataFrame(rows,columns=['symbol', 'date','prevclose', 'open','high','low', 'close','vwap','volume','turnover','deliverableqty','percentdelivery'])

#### changing datatypes
df['date'] = pd.to_datetime(df['date'])
df['close'] = df['close'].astype(np.float64)
df['open'] = df['open'].astype(np.float64)
df['volume'] = df['volume'].astype(np.float64)
df['percentdelivery'] = df['percentdelivery'].astype(np.float64)


################################################################################################### getting data ready
plt.subplot(3, 1, 1) 
plt.plot(df['date'].values,df['close'].values,color='green',alpha=0.5,)
plt.plot(df['date'].values,df['open'].values,color='red',alpha=0.5,)

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is line plot using matplotlib') 

plt.subplot(3, 1, 2) 
plt.plot(df['date'].values,df['volume'].values,color='red',alpha=0.5,)

plt.subplot(3, 1, 3) 
plt.plot(df['date'].values,df['percentdelivery'].values,color='red',alpha=0.5,)

plt.show()