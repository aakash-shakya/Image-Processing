#!/usr/bin/python3

# padding in an image ( Making Borders of an Image )

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blue = [255,0,0]

img1 = cv.imread('./images/kakashi.jpeg')
replicate = cv.copyMakeBorder(img1, 10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10,10,10,10,cv.BORDER_REFLECT)
reflect_101 = cv.copyMakeBorder(img1, 10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10,10,10,10,cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=blue)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title("Original")
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title("Replicate")
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title("reflect")
plt.subplot(234),plt.imshow(reflect_101,'gray'),plt.title("reflect_101")
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,'gray'),plt.title("constant")

plt.show()
