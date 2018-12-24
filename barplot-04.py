################################################################################################
#	name:	barplot-04.py
#	desc:	Simple bar plot with options - horizontal bar
#	date:	2018-07-02
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
sales =  [71, 91, 56, 66, 52, 27]

plt.barh(np.arange(len(drinks)), sales,label="Jagur", color='b',edgecolor='b')

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is bar plot using matplotlib') 
# plt.legend(drinks)
plt.legend(loc=2)

# Saving image
plt.savefig('barplot-04.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')