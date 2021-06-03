import cv2
import numpy as np

'''
    change path of the image location
'''

path1 = 'itachi.jpg'
path2 = 'naruto.jpg'

image1 = cv2.imread(path1)
image2 = cv2.imread(path2)

image1_resize = cv2.resize(image1,(256,256))
image2_resize = cv2.resize(image2,(256,256))

_and = cv2.bitwise_and(image1_resize,image2_resize,mask = None)
_or = cv2.bitwise_or(image1_resize,image2_resize,mask = None)
_xor = cv2.bitwise_xor(image1_resize,image2_resize,mask = None)
_not = cv2.bitwise_not(image1_resize,mask = None)

cv2.imshow('bitwise and',_and)
cv2.imshow('bitwise or',_or)
cv2.imshow('bitwise xor',_xor)
cv2.imshow('bitwise not',_not)

cv2.waitKey(0)
cv2.destroyAllWindows()