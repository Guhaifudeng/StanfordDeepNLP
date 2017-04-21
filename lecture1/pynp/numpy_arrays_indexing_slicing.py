#!python27
import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print a

b = a[:2,1:3] # 1-2,2-3 2x2 or 0-1,1-2
# 2 3
# 6 7
print b

print a[0,1]#2
b[0,0] = 122
print a

