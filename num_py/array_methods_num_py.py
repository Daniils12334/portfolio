import numpy as np

a= np.array([[1,2,3,8],
            [4,5,6,7]])
# IMPORTANT to say a= cause otherway won,t cahnge anything
a = np.append(a, [1,3,4])
# IMPORTANT to say a= cause otherway won,t cahnge anything

a = np.insert(a, 3, [4,5,6,7]) # insert values from 3 position of the array 

print(a)

np.delete(a, 1) # gonna delete first element in this case [1,2,3,8] ---> [1,3,8]
np.delete(a, 0, 0)  # deletes the first row (axis=0) from array 'a'
np.delete(a, 0, 1)  # deletes the first column (axis=1) from array 'a'
