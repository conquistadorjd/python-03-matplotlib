################################################################################################
#	name:	heatmap-01.py
#	desc:	heatmap with matplotlib
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np

print('*** Program Started ***')

uniform_data = np.random.rand(10, 12)

# fig, ax = plt.subplots()
# im = ax.imshow(uniform_data)

########## second way
# fig, ax = plt.subplots()
plt.imshow(uniform_data)


# Saving image
plt.savefig('heatmap-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')