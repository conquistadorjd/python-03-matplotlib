################################################################################################
#	name:	barplot-01.py
#	desc:	Simple bar plot with different data
#	date:	2018-07-02
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
sales =  [71, 91, 56, 66, 52, 27]

plt.bar(np.arange(len(drinks)), sales,label="Jagur")

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is bar plot using matplotlib') 
# plt.legend(drinks)
plt.legend(loc=2)

# Saving image
plt.savefig('barplot-02.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')