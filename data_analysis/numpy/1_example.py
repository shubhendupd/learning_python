import numpy as np

#arr = np.array(([1,2,3,4,5],[1,2,3,4,5]))

#print(arr)

#print(type(arr))

#ndim attributes provides a way to return an integer that tell us how many dimensions that array have.
'''
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

'''

# "ndmin" argumnet let us define number of dimensions
'''
arr = np.array([1,2,3,4], ndmin = 5)

print(arr)

print("number of dimensions: ", arr.ndim)

'''

from numpy import random

x = random.normal(loc=0, scale=1, size=(2, 3))
print(x)
