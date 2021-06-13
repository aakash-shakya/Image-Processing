#!/usr/bin/python3

# Laplacian of an Image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/kakashi.jpeg')
image = cv.resize(image,(400,500))

#using 2nd order laplacian operator without Gaussian Filter
imageWOb = cv.Laplacian(image,cv.CV_64F, ksize=1)

#using gaussian filter to remove noise
imagewb = cv.GaussianBlur(image,(3,3),0)
imagewb = cv.Laplacian(image,cv.CV_64F,ksize=1)

plt.subplot(131),plt.imshow(image),plt.title("input")
plt.subplot(132),plt.imshow(imageWOb),plt.title("output : 2nd ord Derivateive w/o Blur")
plt.subplot(133),plt.imshow(imagewb),plt.title("Output: 2nd ord Derivative")

plt.show()