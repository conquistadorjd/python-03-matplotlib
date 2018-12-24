from matplotlib import pyplot as plt

# freq='D' can be 'H' for hourly, 'M' for monthly
rng = pd.date_range('1/1/2018', periods=20, freq='D')
y= np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5])
print('rng :', rng)
print('y :', y)