# LOG TRANSFORMATION OF IMAGE

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/itachi.jpg')
c = 255/np.log(1 + np.max(img))
log_image=c * (np.log(img+1))
log_image = np.array(log_image,dtype=np.uint8)

plt.imshow(img)
plt.show()
plt.imshow(log_image)
plt.show()
