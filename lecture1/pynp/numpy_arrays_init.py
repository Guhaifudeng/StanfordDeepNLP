import numpy as np
a = np.zeros((2, 2))
print a

#b = ones((1, 2))wrong
print type(a)

b = np.ones((1, 2))
print b

c = np.full((2, 2), 7)
print c

d = np.eye(2)
print d

e = np.random.random((2, 2))
print e

f = np.arange(1,2,0.1)
print f

g = np.linspace(1., 4., 6)
print g
