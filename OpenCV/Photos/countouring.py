import cv2 as cv
import numpy as np

img=cv.imread('tim.jpg')
cv.imshow('tim',img)

blank= np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny =cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#threshold tries to  binarize the image <125 =0
ret,thresh = cv.threshold(gray,80,255,cv.THRESH_BINARY)
cv.imshow('binary',thresh)



contours, hierarchies= cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countours found')


cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow('counters drawn', blank)


cv.waitKey(0)
cv.destroyAllWindows()