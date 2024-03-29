import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/naruto.jpg',0)

kernel = np.ones((13,13),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(131),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(132),plt.imshow(opening,'gray'),plt.title('OPENING')
plt.subplot(133),plt.imshow(closing,'gray'),plt.title('CLOSING')
plt.show()