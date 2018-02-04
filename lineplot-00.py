from matplotlib import pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5,6,7,8,9,10])
y= np.array([1,2,3,4,5,6,7,8,9,10])

#plt.scatter(x,y)
plt.plot(x,y,color='green',alpha=0.5,)

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is line plot using matplotlib') 

plt.show()