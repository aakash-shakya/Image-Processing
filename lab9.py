#!/usr/bin/python3

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/naruto.jpg')
image = cv.resize(image,(400,400))

gauss_mask = cv.GaussianBlur(image,(9,9),0)
image_sharp = cv.addWeighted(image,2,gauss_mask,-1,0)

kernel = np.array([[-1,-1,-1],
                [-1,8,-1],
                [-1,-1,-1]])

image_hpf = cv.filter2D(image,-1,kernel)

plt.subplot(131),plt.imshow(image),plt.title("input image")
plt.subplot(132),plt.imshow(image_sharp),plt.title("output: sharpen")
plt.subplot(133),plt.imshow(image_hpf),plt.title("output : High pass filter")

plt.show()