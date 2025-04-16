import numpy as np

a = np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18],
              [19,20,21,22,23,24]])

np.save("other/myarray.npy", a) # creates npy file. cant read cause it is binary
np.savetxt("other/myarray.csv", a, delimiter = ",") # creates npy file. cant read cause it is binary



array_loaded = np.load("other/myarray.npy")
array_loaded = np.loadtxt("other/myarray.csv", delimiter = ",")

print(array_loaded)
