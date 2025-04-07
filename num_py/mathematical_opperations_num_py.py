import numpy as np

l1 = [1,6,7,3,4,5]
l2 = [4,5,8,5,3,0]

a1 = np.array(l1)
a2 = np.array(l2)


#python lists
#unsupport / + -
print(l1 * 5) # repeats list 5 times [1,6,7,3,4,5, ... 1,6,7,3,4,5]
#numpy lists
#support all math operators
print(a1 * 5) # multipile each element of the array by 5 [ 5 30 35 15 20 25]
print(a1 + a2) # pluses each element [ 5 11 15  8  7  5]

x1 = np.array([1,2,3])
x2 = np.array([[1],[2]])

print(x1+x2)
#output
# [[2 3 4] 1+1 2+1 3+1
#  [3 4 5]] 1+2 2+2 3+2
# not gonna work if x2 will be smthng like ([[1,1],[2,3]])

n = np.array([[1,3,4],[5,8,6]])
print(np.sqrt(n))
    #np.cos
    #np.tan
    #np.arctan
    #np.exp
    #np.log10
    #and etc

