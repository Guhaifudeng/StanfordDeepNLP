import numpy as np
a = np.array([[1,2],[3,4],[5,6],[7,8]])
print a

print a[[0,1,2],[0,1,0]]

print a[[0,0],[1,1]]
print np.array([a[0,1], a[0,1]])

print '--------------------------'

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print b
c =np.array([0, 2, 0, 1])
print type(np.arange(4))
print b[np.arange(4), c]

b[np.arange(4),c] +=10
print b
d = b ** 2
print type(d),"\n",d


