import numpy as np
x = np.array([[1,2,3],[4,4,6]])
y = np.array([[4,5],[7,8],[2,3]])
v = np.array([9,10])
w = np.array([11,12])
# inner pruduct of vectors
print v.dot(w) #octave sum(v.*w)
print np.dot(v,w)
#matrx/vector product
print y.dot(v)
print np.dot(y,v)
# matrx product
print x.dot(y) #2x3 2x3 wrong
print np.dot(x,y)


