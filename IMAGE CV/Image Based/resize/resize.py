import cv2
import imutils

img = cv2.imread('ss.jpg')
resizedImg = imutils.resize(img,width=500)

cv2.imshow('OriginalImage2.jpg',img)
cv2.imshow('resized.jpg',resizedImg)
cv2.imwrite('resizedImage2.jpg', resizedImg)

