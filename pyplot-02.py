################################################################################################
#	name:	pyplot-02.py
#	desc:	Plotting multiple datasets on single plot
#	date:	2018-07-1
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

x1= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
y1= np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])

x2= np.arange(10,20,1) 
y2= np.arange(10,60,5) 
plt.plot(x2,y2,x1,y1)
# plt.plot([1,2,3,4,5],[1,2,3,4,5])

# Saving image
# plt.savefig('pyplot-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')