import cv2 as cv

img=cv.imread('tim.jpg')
cv.imshow('tim',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#thresholding--convert to binary

#simple Thresholding

threshold,thresh=cv.threshold(gray,80,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold,thresh_inverse=cv.threshold(gray,80,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh inverse',thresh_inverse)

#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,9,-9)
cv.imshow('adaptive thresholding',adaptive_thresh)


cv.waitKey(0)