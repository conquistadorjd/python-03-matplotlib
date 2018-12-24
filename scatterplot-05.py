from matplotlib import pyplot
import numpy as np

x= np.array([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
y= np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
pyplot.scatter(x,y,c='none')
pyplot.plot([1,2,3,5,6,8,3,4])
for i,j in zip(x,y):
    ax.annotate(str(i),xy=(i,j))

pyplot.show()