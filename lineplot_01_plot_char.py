################################################################################################
#   name:   lineplot_01_plot_char.py
#   desc:   various parameters
#   date:   2018-12-24
#   Author: conquistadorjd
###################################################################################################################
# version control
# 2018-12-24    :   First version created in python3.6
###################################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

x= np.array([1,2,3,4,5,6,7,8,9,10])
y= np.array([1,2,4,9,15,18,22,29,39,50])

#plt.scatter(x,y)
plt.plot(x,y,color='green',alpha=0.5,label="test graph")

plt.legend(loc=2)  
plt.title('linear graph')

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')

plt.xlim( 1, 20 )  # set the xlim to xmin, xmax
plt.ylim( 1, 20 )    # set the ylim to ymin, ymax

plt.yticks( [5,15,20] )
plt.xticks( [5,7,15,20,25], ('Tom', 'Dick', 'Harry', 'Sally', 'Sue') )

plt.yscale('linear')  # The available scales are: ‘linear’ | ‘log’ | ‘logit’ | ‘symlog’
plt.xscale('linear')  # The available scales are: ‘linear’ | ‘log’ | ‘logit’ | ‘symlog’


plt.hlines(y=15, xmin=1, xmax=15,linewidth=0.5, color='g')
plt.vlines(x=10, ymin=1, ymax=15,linewidth=0.5, color='g')

plt.grid(color='g', linestyle='--', linewidth=0.5,markevery=int)

# plt.fill_betweenx(y, x1, x2=0, where=None, step=None, hold=None, data=None, **kwargs)

# Adding a point on graph
x1=[5,15.5]
y1=[5,15.5]
plt.scatter(x1,y1,color='red')

plt.savefig('lineplot_01_plot_char.png')

plt.show()



print('*** Program ended ***')