################################################################################################
#	name:	heatmap-04.py
#	desc:	heatmap with seaborn for stock market
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import date
import datetime

print('*** Program Started ***')

df = pd.read_csv('15-06-2016-TO-14-06-2018HDFCBANKALLN.csv')
df['PChange'] = (df['Close Price'] - df['Prev Close'])/df['Prev Close']*100
df.Date=pd.to_datetime(df.Date)
df = df[df['Date']>datetime.date(2018,1,1)]
df['year']=df.Date.dt.strftime('%Y')
df['month']=df.Date.dt.strftime('%m')
df['day']=df.Date.dt.strftime('%d')
print(df)
df2 = df.pivot( "month", "day","PChange")
print(df2)
# Saving image
# plt.savefig('heatmap-04.png')

# In case you dont want to save image but just displya it
# plt.show()

print('*** Program ended ***')