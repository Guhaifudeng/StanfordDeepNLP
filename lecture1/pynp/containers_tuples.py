d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print type(t)    # Prints "<type 'tuple'>"
print d[t]       # Prints "5"
print d[(1, 2)]  # Prints "1"

t = {( x+1,x): x for x in range(10)}
print type(t)
idx = (4,5)
<<<<<<< HEAD
#print t[idx] # keyError
print t[(5,4)]

=======
#print t[idx] #keyError
print t[(5,4)]
>>>>>>> 0c6ba31874653d1a200fdf5af32c15462c4027da
