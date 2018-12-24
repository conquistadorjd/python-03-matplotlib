################################################################################################
#	name:	timeseries_simple_with_pointer.py
#	desc:	Plots buy and sell signal on line chart
#	date:	2018-06-15
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


print('*** Program Started ***')

df = pd.read_csv('15-06-2016-TO-14-06-2018HDFCBANKALLN.csv')

# ensuring only equity series is considered
df = df.loc[df['Series'] == 'EQ']

# Converting date to pandas datetime format
df['Date'] 	= pd.to_datetime(df['Date'])
df['SMA5'] 	= df["Close Price"].rolling(20).mean()
df['SMA20'] = df["Close Price"].rolling(100).mean()

#Using matplotlib to add required columns
plt.plot(df['Date'], df['Close Price'],linewidth=0.5,color='black')
plt.plot(df['Date'], df['SMA5'],linewidth=0.5,color='blue')
plt.plot(df['Date'], df['SMA20'],linewidth=0.5,color='c')

df['SMA5']		=df['SMA5'].fillna(0)
df['SMA20']		=df['SMA20'].fillna(0)

#Identifying the buy/sell zone
df['Buy'] = np.where( (df['SMA5']> df['SMA20']), 1, 0)
df['Sell'] = np.where( (df['SMA5']< df['SMA20']), 1, 0)

##identify buy sell signal
df['Buy_ind'] = np.where( (df['Buy'] > df['Buy'].shift(1)),1,0)
df['Sell_ind'] = np.where( (df['Sell'] > df['Sell'].shift(1)),1,0)
# print(df.dtypes)
# print(df.head(20))

## plotting the buy and sellsignals on graph
plt.scatter(df.loc[df['Buy_ind'] ==1 , 'Date'].values,df.loc[df['Buy_ind'] ==1, 'Close Price'].values, label='skitscat', color='green', s=25, marker="^")
plt.scatter(df.loc[df['Sell_ind'] ==1 , 'Date'].values,df.loc[df['Sell_ind'] ==1, 'Close Price'].values, label='skitscat', color='red', s=25, marker="v")

## Adding labels
plt.xlabel('Date')  
plt.ylabel('Close Price')  
plt.title('HDFC stock price with buy and sell signal') 

# Saving image
plt.savefig('HDFC with SMA 20-100 Buy sell.png')

# In case you dont want to save image but just displya it
# plt.show()
# df.to_csv('temp_hdfc.csv')
print('*** Program ended ***')