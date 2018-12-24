################################################################################################
#	name:	timeseries_OHLC.py
#	desc:	creates OHLC graph
#	date:	2018-06-15
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
# import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from matplotlib.finance import candlestick_ohlc
# from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

print('*** Program Started ***')

df = pd.read_csv('15-06-2016-TO-14-06-2018HDFCBANKALLN.csv')

# ensuring only equity series is considered
df = df.loc[df['Series'] == 'EQ']

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
df["Date"] = df["Date"].apply(mdates.date2num)

# Creating required data in new DataFrame OHLC
ohlc= df[['Date', 'Open Price', 'High Price', 'Low Price','Close Price']].copy()
# In case you want to check for shorter timespan
# ohlc =ohlc.tail(60)

f1, ax = plt.subplots(figsize = (10,5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# Saving image
plt.savefig('OHLC HDFC.png')

# In case you dont want to save image but just displya it
#plt.show()

print('*** Program ended ***')