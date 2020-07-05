import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread('images/face_1.jpg')

# Convert the image into grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Detect the faces in the image
faces = cascade.detectMultiScale(img_gray, 1.1, 4)


# Draw rectangles around the faces
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (159, 35, 132), 4)


# Display the image with rectangles
cv2.imshow('Face_Detection', img)
cv2.waitKey(0)
