#!python27
import numpy as np
x = np.array([[1,2,3],[3,4,5]])
print np.sum(x)
print np.sum(x,axis = 0)# column
print np.sum(x,axis = 1)# row
