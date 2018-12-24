################################################################################################
#	name:	barplot-06.py
#	desc:	stacked bar plot 
#	date:	2018-07-02
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
jagur =  [71, 91, 56, 66, 52, 95]
rangerover =  [60, 50, 70, 85, 69, 27]
jaguryerr =  [5, 5, 5, 5, 5, 5]
rangerovererr =  [5, 5, 5, 5, 5, 5]
width = 0.25

## simple way of doing this
# plt.bar(np.arange(len(drinks)), jagur,+width,align='edge',label="Jagur", color='r',edgecolor='r',yerr=jaguryerr)
# plt.bar(np.arange(len(drinks)), rangerover,-width ,align='edge',label="Range Rover", color='b',edgecolor='b',yerr=rangerovererr)


### Another way of doing same thing
plt.bar(np.arange(len(drinks)), jagur,width,align='edge',label="Jagur", color='#c11f9e',edgecolor='r',yerr=jaguryerr)
plt.bar(np.arange(len(drinks))+width, rangerover,width ,align='edge',label="Range Rover", color='b',edgecolor='b',yerr=rangerovererr)
plt.bar(np.arange(len(drinks))+width+width, rangerover,width ,align='edge',label="Land Rover", color='c',edgecolor='c',yerr=rangerovererr)

print(type(np.arange(len(drinks))))
print(type(range(len(drinks))))
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('Monthly sales of cars') 
# plt.legend(drinks)
plt.legend(loc=2)

# Saving image
plt.savefig('barplot-06.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')