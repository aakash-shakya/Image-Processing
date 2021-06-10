#!/usr/bin/python3

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/naruto.jpg')
image = cv.resize(image,(400,400))
cv.imshow("input",image)

gauss_mask = cv.GaussianBlur(image,(9,9),0)
image_sharp = cv.addWeighted(image,2,gauss_mask,-1,0)

cv.imshow("output: sharpen",image_sharp)

kernel = np.array([[-1,-1,-1],
                [-1,8,-1],
                [-1,-1,-1]])

# high pass filters can also be obtained by substraticng a low pass filtered image
# from original image

image_hpf = cv.filter2D(image,-1,kernel)
cv.imshow("output : High pass filter ", image_hpf)
cv.waitKey(0)
cv.destroyAllWindows()  