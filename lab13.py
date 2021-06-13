import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./images/kakashi.jpeg',0)

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations=1)
dilation = cv.dilate(img,kernel,iterations=1)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(erosion,'gray'),plt.title('erosion')
plt.subplot(233),plt.imshow(dilation,'gray'),plt.title('dilation')

plt.show()