# LAB 7: Histogram Equalization (Also plot the histogram of both images)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/kakashi.jpeg',0)
img_1 = cv2.resize(img,(256,256))

equ = cv2.equalizeHist(img_1)
#res = np.hstack((img_1,equ))

histr1 = cv2.calcHist([img_1], [0], None, [256], [0, 256])
histr2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

plt.subplot(221),plt.imshow(img_1),plt.title('Light_Img')
plt.subplot(222),plt.imshow(equ),plt.title('Dark_Img')
plt.subplot(223),plt.plot(histr1),plt.title("Hist")
plt.subplot(224),plt.plot(histr2),plt.title("HistEqualizer")

plt.show()
