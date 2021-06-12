# LAB 1: Opening an image, printing the size and converting it into grayscale.

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('./images/naruto.jpg')
cv2.imshow('image',img)
img1 = cv2.imread('./images/itachi.jpg',0)
cv2.imshow('g',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
print(img[:,:,0])
print(img1.shape)
print(img1[:,:])
