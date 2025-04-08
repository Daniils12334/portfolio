import numpy as np

a1 = np.array([[1,2,3,4,5,6],
              [5,6,7,3,9,6]])
a2 = np.array([[80,58,38,58,66,14],
              [61,21,11,54,93,18]])



a = np.concatenate((a1,a2), axis = 1) #axis = 0 - will create 4 different arrays. #axis = 1 - will append 0 array from a1 with a2

a = np.stack((a1, a2))   # stacks arrays along a new axis (by default axis=0), increasing dimension by 1
a = np.vstack((a1, a2))  # vertically stacks arrays (along axis=0), like putting rows on top of each other
a = np.hstack((a1, a2))  # horizontally stacks arrays (along axis=1 for 2D), like adding columns side by side


print(a)
print(np.split(a, 1, axis = 0)) # split into 1 array
print(np.array_split(a1, 4, axis = 0)) # split into 2 arrays


# a1 = np.array([[1, 2, 3],
            #    [4, 5, 6]])
# 
# np.array_split(a1, 3, axis=0)  # Режем по строкам → 3 части: 2 полные, 1 пустая/частичная
# 