################################################################################################
#	name:	subplot-01.py
#	desc:	Fsubplot using matplotlib
#	date:	2018-07-1
#	Author:	conquistadorjd
################################################################################################
import matplotlib.pyplot as plt
import numpy as np

print('*** Program Started ***')

t= np.arange(1,17,1) 
y1= np.random.randint(1, 16,size=16)
y2= np.random.randint(1, 32,size=16)
y3= np.random.randint(1, 48,size=16)


ax1 = plt.subplot(311)
plt.plot(t, y1,label="Jagur")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
plt.title('subplot')
# plt.grid(True)
# plt.yscale('log')
# make these tick labels invisible
# plt.setp(ax1.get_xticklabels(), visible=False , fontsize=10)

# share x only
ax2 = plt.subplot(312, sharex=ax1)
plt.plot(t, y2,label="Range Rover")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')
plt.legend(loc=2)  
# plt.title('linear')
# make these tick labels invisible
# plt.setp(ax2.get_xticklabels(), visible=False, fontsize=10)

# share x and y
ax3 = plt.subplot(313, sharex=ax1)
plt.plot(t, y3, label="Land Rover")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
# make these tick labels visible with required font size
# plt.setp(ax3.get_xticklabels(), visible=True, fontsize=10)

# Saving image
plt.savefig('subplot-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')