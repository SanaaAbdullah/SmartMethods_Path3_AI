import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('images/sky.jpg')

img_blur = blur = cv2.blur(img,(10,10))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_edge = cv2.Canny(img,100,200)

img_contrast = cv2.convertScaleAbs(img, alpha=1.3, beta=40)

img_red = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# I plot the images to be two rows and three columns.
# Also I convert the image into B, G, R colors because plot method works with GBR image
plt.subplot(231),plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR)),plt.title('Original')
plt.subplot(232),plt.imshow(cv2.cvtColor(img_blur, cv2.COLOR_RGB2BGR)),plt.title('Blurred')
plt.subplot(233),plt.imshow(cv2.cvtColor(img_gray, cv2.COLOR_RGB2BGR)),plt.title('Gray_Scale')
plt.subplot(234),plt.imshow(cv2.cvtColor(img_edge, cv2.COLOR_RGB2BGR)),plt.title('Edge_Detection')
plt.subplot(235),plt.imshow(cv2.cvtColor(img_contrast, cv2.COLOR_RGB2BGR)),plt.title('Increase_Contrast')
plt.subplot(236),plt.imshow(cv2.cvtColor(img_red, cv2.COLOR_RGB2BGR)),plt.title('Red')

plt.show()