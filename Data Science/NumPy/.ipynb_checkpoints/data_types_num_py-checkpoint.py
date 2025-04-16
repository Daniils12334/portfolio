import numpy as np

d = {'1': 'A'} # if we enter that in np array, array will be 'object' Ex: [1,d,3]

a = np.array([[1,2,3], [1,2,"Hello"], [1,2,3]]) 
# cant swap into integer by command [],[],[], dtype = np.int32. 
# only if Hello would be [1,2,"5"] or any other integer
                                                                                                
print(a.dtype) # output <U21 means string with less or equal 21 charachters
print(type(a[0][0])) # <class 'numpy.str_'>
print(a[0][0].dtype) # <U1 (string)

#https://numpy.org/devdocs/