from matplotlib import pyplot as plt
import numpy as np

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]  
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('This is bar plot using matplotlib') 
plt.legend(drinks)

# plt.figure(figsize=(7, 3))  
# plt.savefig('power_generated.png')  

plt.show() 