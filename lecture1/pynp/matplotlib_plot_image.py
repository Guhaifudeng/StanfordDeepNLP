import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('cat.jpg')
img_tinted = img * [0.5,0.45,0.45]
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(np.uint8(img_tinted))
plt.show()
