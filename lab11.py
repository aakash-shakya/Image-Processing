#!/usr/bin/python3

# Laplacian of an Image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/itachi.jpg',0)
image = cv.resize(image,(400,500))
cv.imshow("input", image)

#using 2nd order laplacian operator without Gaussian Filter
imageWOb = cv.Laplacian(image,cv.CV_64F, ksize=1)
cv.imshow("output : 2nd ord Derivateive w/o Blur", imageWOb)

#using gaussian filter to remove noise
image = cv.GaussianBlur(image,(3,3),0)
image = cv.Laplacian(image,cv.CV_64F,ksize=1)

cv.imshow("Output: 2nd ord Derivative",image)
cv.waitKey(0)
cv.destroyAllWindows()
