################################################################################################
#	name:	pyplot-03.py
#	desc:	Plotting with line properties
#	date:	2018-07-1
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

print('*** Program Started ***')

x= np.arange(1,17,1) 
y= np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])

plt.plot(x,y,linewidth=1.0, linestyle='--',marker='*',color='g',label='first',animated=True)

# Saving image
plt.savefig('pyplot-03.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')