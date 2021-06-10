#!/usr/bin/python3

# Laplacian of an Image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('./images/naruto.jpg',0)
image = cv.resize(image,(400,500))
cv.imshow("input", image)

image_1= cv.Sobel(image,cv.CV_64F, 1, 0, ksize=1)  # x-direction
image_2 = cv.Sobel(image,cv.CV_64F, 0, 1, ksize=1)  # y-direction

cv.imshow("output1 : sobel X-axis",image_1)
cv.imshow('output2 : sobel Y-axis', image_2)

cv.waitKey(0)
cv.destroyAllWindows()

