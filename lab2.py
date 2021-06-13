import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image_path = 'images/naruto.jpg'

img = cv.imread(image_path,0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

titles = ['original Image','Binary','Binary_INV']
images = [img,thresh1,thresh2]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
