#!/usr/bin/python3

# Sobel of an Image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/naruto.jpg')
image = cv.resize(image,(400,500))

image_1= cv.Sobel(image,cv.CV_64F, 1, 0, ksize=1)  # x-direction
image_2 = cv.Sobel(image,cv.CV_64F, 0, 1, ksize=1)  # y-direction

plt.subplot(131),plt.imshow(image),plt.title("input image")
plt.subplot(132),plt.imshow(image_1),plt.title("output: sobel X-axis")
plt.subplot(133),plt.imshow(image_2),plt.title("output : sobel Y-axis")

plt.show()
