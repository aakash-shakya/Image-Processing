# Power Law Transformation of an Image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1_path = 'images/itachi.jpg'

img1 = cv.imread(img1_path,1)
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img1 = cv.resize(img1,(400,400))

gamma = 2
img2 = np.power(img1,gamma)

gamma = 3
img3 = np.power(img1,gamma)

gamma = 4
img4 = np.power(img1,gamma)

# cv.imshow('input image',img1)
# cv.imshow('gamma 2',img2)
# cv.imshow('gamma 3',img3)
# cv.imshow('gamma 4',img4)

# cv.waitKey()
# cv.destroyAllWindows()

titles = ['original Image','gamma 2','gamma 3','gamma 4']
images = [img1,img2,img3,img4]

for i in range(4):
    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



