################################################################################################
#	name:	barplot-03.py
#	desc:	Simple bar plot with options
#	date:	2018-07-02
#	Author:	conquistadorjd
#   Documentation : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
sales =  [71, 91, 56, 66, 52, 27]
salesyerr =  [5, 5, 5, 5, 5, 5]

# This is with mandatory fields
# plt.bar(np.arange(len(drinks)), sales)
# This is with multiple options
plt.bar(np.arange(len(drinks)), sales, width=0.5, yerr=salesyerr, label="Jagur", color='r',edgecolor='b', fill=True, hatch='*',linestyle='--',align='center')

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is bar plot using matplotlib') 

# plt.legend(drinks)
plt.legend(loc=2)

# Saving image
plt.savefig('barplot-03.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')