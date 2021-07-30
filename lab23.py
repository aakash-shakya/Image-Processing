import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import random

def sp_noise(image,prob):
    output = np.zeros(image.shape, np.uint8)
    thres=1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn=random.random()
            if rdn<prob:
                output[i][j]=0
            elif rdn>thres:
                output[i][j]=255
            else:
                output[i][j]=image[i][j]

    return output

image = cv.imread('./images/kakashi.jpeg',0)
imag= cv.imread('./images/kakashi.jpeg')
noise_img=sp_noise(image,0.2)
n_img=sp_noise(imag,0.2)

plt.subplot(141),plt.imshow(image,cmap="gray")
plt.title("original Image"),plt.xticks([]),plt.yticks([])

plt.subplot(142),plt.imshow(noise_img,cmap="gray")
plt.title("S&P noise Image"),plt.xticks([]),plt.yticks([])

plt.subplot(143),plt.hist(noise_img.ravel(),256,[0,256])
plt.title("Histogram"),plt.xticks([]),plt.yticks([])

dst = cv.fastNlMeansDenoisingColored(n_img,None,10,10,7,21)

plt.subplot(144), plt.imshow(dst)
plt.show()

