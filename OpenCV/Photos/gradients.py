import cv2 as cv
import numpy as np

img=cv.imread('tim.jpg')
cv.imshow('tim',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

#sobel gradient magnitude
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
cv.imshow('sobelx',sobelx)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobely',sobely)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('combined sobel',combined_sobel)

#canny
canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)



cv.waitKey(0)