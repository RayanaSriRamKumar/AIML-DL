import cv2

img = cv2.imread('color.jpg')

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)[1]

cv2.imshow('Original',img)
cv2.imshow('threshold.jpg',thresholdImg)

