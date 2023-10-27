import cv2 as cv


img=cv.imread('tim.jpg')
cv.imshow('tim',img)

#bgr to  grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#bgr to hsv
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#bgr to lab
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)


cv.waitKey(0)