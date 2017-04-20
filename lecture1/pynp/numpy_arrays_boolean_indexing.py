import numpy as np
a = np.array([[1,2],[3,4],[5,6],[7,8]])
bool_idx = (a > 4)
print a
print bool_idx

print a[bool_idx]
print a[a >4]
