################################################################################################
#	name:	barplot-01.py
#	desc:	Simple bar plot
#	date:	2018-07-02
#	Author:	conquistadorjd
################################################################################################
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print('*** Program Started ***')

t= np.arange(1,17,1) 
y1= np.random.randint(1, 16,size=16)
y2= np.random.randint(1, 32,size=16)
y3= np.random.randint(1, 48,size=16)


plt.bar(t, y1,label="Jagur")
# sns.barplot(t, y1,label="Jagur")

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.legend(loc=2)
# plt.title('subplot')
# plt.grid(True)
# plt.yscale('log')
# make these tick labels invisible
# plt.setp(ax1.get_xticklabels(), visible=False , fontsize=10)


# Saving image
plt.savefig('barplot-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')