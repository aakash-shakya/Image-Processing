import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from lab23 import sp_noise

img = cv.imread('./images/kakashi.jpeg')
image = sp_noise(img,0.2)

dst = cv.fastNlMeansDenoisingColored(image,None,10,10,7,21)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()