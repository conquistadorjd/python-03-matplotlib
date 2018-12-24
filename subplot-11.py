################################################################################################
#	name:	subplot-11.py
#	desc:	Subplot using matplotlib
#	date:	2018-12-24
#	Author:	conquistadorjd
################################################################################################
import matplotlib.pyplot as plt
import numpy as np

print('*** Program Started ***')

t= np.arange(1,17,1) 
y1= np.random.randint(1, 16,size=16)
y2= np.random.randint(1, 32,size=16)
y3= np.random.randint(1, 48,size=16)


ax1 = plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=1)
plt.plot(t, y1)

# share x only
ax2 = plt.subplot2grid((3,3), (1,0), colspan=3,rowspan=1,sharex=ax1)
plt.plot(t, y2)


# share x and y
ax3 = plt.subplot2grid((3,3), (2, 0), colspan=3,rowspan=1,sharex=ax1)
plt.plot(t, y3)


# Saving image
plt.savefig('subplot-11.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')