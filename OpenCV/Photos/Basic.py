import cv2 as cv

img=cv.imread('website.jpg')

cv.imshow('panda',img)
#converting to gray scale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#blurring an image
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascading

canny=cv.Canny(blur,60,150)
cv.imshow('canny',canny)
cv.waitKey(0)
