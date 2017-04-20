import numpy as np
v = np.array([1,2,3])
w = np.array([4,5])

print np.reshape(v,(3,1)) * w

x = np.array([[1,2,3],[4,5,6]])
print x+v

print (x.T + w).T

print x * 2
