################################################################################################
#	name:	histogram-01.py
#	desc:	histogram simple example
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

N_points = 100000
n_bins = 20

# Generate a normal distribution, center at x=0 and y=5
# x = np.random.randn(N_points)
# y = .4 * x + np.random.randn(100000) + 5
# print(x)
# print(y)
# # plt.hist(x, bins=n_bins)
# plt.hist(x, bins='auto')

rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))

plt.hist(a, bins='auto',color='#1dd5e2',facecolor='red')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")

# Saving image
plt.savefig('histogram-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')