import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
#set the first such subplot as active.
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('sine')
# Set the second subplot as active, and make the second plot
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine')

plt.subplot(2,1,1) # 3 is wrong
plt.plot(x,y_tan)
plt.title('tan')
plt.show()
