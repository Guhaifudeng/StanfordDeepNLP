#!python27
import numpy as np

x = np.array([[1,2],[2,3],[3,4]])
print x
print x.T

# note that taking the transpose of a rank 1 array dose nothing
v = np.array([1,2,3])
print v
print v.T

# (1,3)

v_ma = np.array([1,2,3])
# print v_ma[0].T wrong list
print np.reshape(v_ma,(1,3))
print np.shape(v_ma)
v_ma = np.reshape(v_ma,(1,3))
print np.shape(v_ma)
