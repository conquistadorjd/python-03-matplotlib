################################################################################################
#	name:	barplot-05.py
#	desc:	stacked bar plot 
#	date:	2018-07-02
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
sales =  [71, 91, 56, 66, 52, 27]
inquiry =  [60, 50, 70, 66, 52, 27]
salesyerr =  [5, 5, 5, 5, 5, 5]
inquiryerr =  [5, 5, 5, 5, 5, 5]

plt.bar(np.arange(len(drinks)), sales,width=0.5,label="Jagur", color='r',edgecolor='r',yerr=salesyerr)
plt.bar(np.arange(len(drinks)), inquiry,bottom=sales,width=0.5,label="Range Rover", color='b',edgecolor='b',yerr=inquiryerr)

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is bar plot using matplotlib') 

# plt.legend(drinks)
plt.legend(loc=2)

# Saving image
plt.savefig('barplot-05.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')