#!python27
from scipy.misc import imread, imsave, imresize
#import imread wrong
# You might need to install PIL or Pillow.
img = imread('cat.jpg')
print "dtype:",img.dtype, "shape:",img.shape

print img
# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively
img_tinted = img * [1, 0.95, 0.9]
print img_tinted
# Resize the tinted image to be 200 by 200 pixels.
img_tinted = imresize(img_tinted,(200,200))
imsave('cat_tinted.jpg',img_tinted)
