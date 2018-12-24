################################################################################################
#	name:	timeseries_simple.py
#	desc:	Plots line chart using 'Close Price' 
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
df['Date'] = pd.to_datetime(df['Date'])

# Using matplotlib to add required columns
plt.plot(df['Date'], df['Close Price'])

# Adding labels
plt.xlabel('Date')  
plt.ylabel('Close Price')  
plt.title('Simple time series plot for HDFC') 

# Saving image
plt.savefig('Simple time series plot for HDFC.png')

# In case you dont want to save image but just displya it
#plt.show()

print('*** Program ended ***')