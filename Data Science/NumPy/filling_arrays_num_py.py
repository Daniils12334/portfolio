import numpy as np

a = np.full((2,3,4), 9)  
print(a)
#output
# [[[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]
# 
#  [[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]]

a = np.zeros((10,4,2)) # fill array with zeros.

a = np.ones((10,5,2)) # fill with 1.

a = np.empty((5,5,5)) # allocate memory, just reserve space 5,5,5 array for future operations
# output is just adresses from memory
# faster then filling with zeros
print(a)

x_values = np.arange(0, 1000, 5) # random values from 0 to 1000 with step size 5 #0 5 10 15 20 25 30 and etc until 995
x_values = np.linspace(0,1000,2) # from 0 to 1000 2 values, like split in x values if we enter 0,1001, 1000 output will be [0. 1. 2. ... 998. 999. 1000.]
print(x_values)

print(np.inf)  # for situations when there is division by zero (inf = infinity)
print(np.nan)  # for undefined or unrepresentable values (nan = not a number)
print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10]) / 0))
