#!python27
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:

row_r1 = a[1,:]
row_r2 = a[1:2,:]
print row_r1, row_r1.shape, type(row_r1)
print row_r2, row_r2.shape, type(row_r2)

col_c1 = a[:, 1]
col_c2 = a[:,1:2]
print col_c1,col_c1.shape
print col_c2,col_c2.shape

