# LAB 6: Plotting the histogram of an Image(Check for normal image, low contrast, dark image)

import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('./images/naruto.jpg', 0)
img2 = cv2.imread('./images/itachi.jpg', 0)
img3 = cv2.imread('./images/kakashi.jpeg', 0)

histr1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
histr2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
histr3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

plt.subplot(241),plt.imshow(img1),plt.title('Normal_Img')
plt.subplot(242),plt.imshow(img2),plt.title('Dark_Img')
plt.subplot(243),plt.imshow(img3),plt.title('Light_Img')

plt.subplot(245),plt.plot(histr1),plt.title('Hist_Normal_Img')
plt.subplot(246),plt.plot(histr2),plt.title('Hist_Dark_Img')
plt.subplot(247),plt.plot(histr3),plt.title('Hist_Light_Img')

plt.show()
