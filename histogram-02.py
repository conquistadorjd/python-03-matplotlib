################################################################################################
#	name:	histogram-02.py
#	desc:	histogram simple example
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
# plt.hist(x,  bins='auto', density=True, facecolor='g', alpha=0.75) 
plt.hist(x, 50, density=True, facecolor='g', alpha=0.75,cumulative=False,orientation='vertical', log=True) 

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)

# Saving image
plt.savefig('histogram-02.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')