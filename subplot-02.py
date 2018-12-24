################################################################################################
#	name:	subplot-02.py
#	desc:	Subplot using matplotlib grid 2*2
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
y4= np.random.randint(1, 48,size=16)


ax1 = plt.subplot(221)
plt.plot(t, y1,label="Jagur")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
plt.title('subplot')
# make these tick labels invisible
# plt.setp(ax1.get_xticklabels(), visible=False , fontsize=10)

# share x only
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
plt.plot(t, y2,label="Range Rover")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
plt.title('subplot')
# make these tick labels invisible
# plt.setp(ax2.get_xticklabels(), visible=False, fontsize=10)

# share x and y
ax3 = plt.subplot(223,sharex=ax1, sharey=ax1)
plt.plot(t, y3,label="Land Rover")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
# plt.title('subplot')
# make these tick labels visible with required font size
# plt.setp(ax3.get_xticklabels(), visible=True, fontsize=10)

# share x and y
ax4 = plt.subplot(224,sharex=ax1, sharey=ax1)
plt.plot(t, y4,label="Tata Motors")
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
# plt.title('subplot')
# make these tick labels visible with required font size
# plt.setp(ax3.get_xticklabels(), visible=True, fontsize=10)

# Saving image
plt.savefig('subplot-02.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')