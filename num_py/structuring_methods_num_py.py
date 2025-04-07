import numpy as np

a = np.array([[1,2,3,4,5,6],
              [5,6,7,3,9,6],
              [80,58,38,58,66,14],
              [61,21,11,54,93,18]])

print(a.shape) # output (4, 6)
print(a.reshape((24,-1))) # means taht num py automatically change column count output is [[ 1] [ 2] [ 3] ...
print(a.reshape((24,))) # [ 1  2  3  4  5  6  5  6  7  3  9  6 80 58 38 58 66 14 61 21 11 54 93 18]
print(a.reshape((4,2,3))) 
# [[[ 1  2  3]
#   [ 4  5  6]]
# 
#  [[ 5  6  7]
#   [ 3  9  6]]
# 
#  [[80 58 38]
#   [58 66 14]]
# 
#  [[61 21 11]
#   [54 93 18]]]

#IMPOERTANT remember a = np......

a.resize((10,2)) # deletes last 4 elements, cose summ of all elements is 24 != 20 if elements will be > 24, fill array with zeros
print(a)
var1 = a.flatten() # creates listed copy of array [ 1  2  3  4  5  6  5  6  7  3  9  6 80 58 38 58 66 14 61 21 11 54 93 18] other cahnges will cahnge copyu of array, not original one
var1 = a.ravel() # shows array as [ 1  2  3  4  5  6  5  6  7  3  9  6 80 58 38 58 66 14 61 21 11 54 93 18] other cahnges will cahnge original array

var = [v for v in a.flat] # [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(5), np.int64(6), np.int64(7), ...
print(var)

print(a.transpose()) # swap columns to show variables 1 instead of 1 2 ... also equals with a.T
                                                    # 2
                                                    # ...

# np.swapaxes(a, axis1, axis2) np.swapaxes returns a view of the array with two specified axes interchanged (swapped).
# better for big arays
