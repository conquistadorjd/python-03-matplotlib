################################################################################################
#	name:	heatmap-02.py
#	desc:	heatmap with seaborn
#	date:	2018-07-03
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

print('*** Program Started ***')

sns.set()
np.random.seed(0)
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

# Saving image
plt.savefig('heatmap-02.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')