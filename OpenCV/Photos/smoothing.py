import cv2 as cv

img=cv.imread('tim.jpg')
cv.imshow('tim',img)

#averaging

average=cv.blur(img,(5,5))
cv.imshow('average blur',average)

#guassain blur

gauss=cv.GaussianBlur(img,(3,3),1)
cv.imshow('guassian',gauss)

#median blur

median=cv.medianBlur(img,3)
cv.imshow('median',median)

#bilateral blurring
bilateral=cv.bilateralFilter(img,15,15,15)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)
