from matplotlib import pyplot as plt
import numpy as np

x= np.array([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
y= np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])

plt.scatter(x,y,marker='s',color='green', edgecolors='red',alpha=0.7,)

x2= np.array([1,2,2,4])
y2= np.array([1,2,3,4])

plt.plot(x2,y2,color='green',alpha=0.5,)



plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is scatter plot using matplotlib') 

plt.show()