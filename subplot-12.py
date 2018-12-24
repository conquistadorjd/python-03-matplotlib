################################################################################################
#	name:	subplot-12.py
#	desc:	Subplot using matplotlib
#	date:	2018-12-24
#	Author:	conquistadorjd
################################################################################################
import matplotlib.pyplot as plt
import numpy as np

print('*** Program Started ***')

t= np.arange(1,17,1) 
t2= np.arange(1,49,1) 
y1= np.random.randint(1, 16,size=16)
y2= np.random.randint(1, 32,size=48)
y3= np.random.randint(1, 48,size=16)
y4= np.random.randint(1, 64,size=16)
y5= np.random.randint(1, 124,size=16)

ax1 = plt.subplot2grid((5,3), (0,0), colspan=3, rowspan=1)
plt.plot(t, y1)

ax2 = plt.subplot2grid((5,3), (1,0), colspan=2,rowspan=1)
plt.plot(t2, y2)

ax3 = plt.subplot2grid((5,3), (1, 2), colspan=2,rowspan=2,sharex=ax1)
plt.plot(t, y3)

ax4 = plt.subplot2grid((5,3), (2, 0), colspan=2,rowspan=1)
plt.plot(t, y4)

ax5 = plt.subplot2grid((5,3), (3, 0), colspan=3,rowspan=2,sharex=ax1)
plt.plot(t*2, y5)

# ax6 = plt.subplot2grid((5,3), (4, 0), colspan=3,rowspan=1,sharex=ax1)
# plt.plot(t, y3)

# Saving image
plt.savefig('subplot-12.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')