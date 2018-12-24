################################################################################################
#	name:	heatmap-03.py
#	desc:	heatmap with seaborn
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

print('*** Program Started ***')

sns.set()
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
# print(flights)
# print(type(flights))

# cust_color = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
# BuGn_r,Blues,BrBG,cubehelix,sns.cubehelix_palette(8),sns.light_palette("green"),sns.light_palette("navy", reverse=False)

ax = sns.heatmap(flights,annot=False,linewidths=0.0,cbar=True,cmap="BuGn_r")

# Saving image
plt.savefig('heatmap-03.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')