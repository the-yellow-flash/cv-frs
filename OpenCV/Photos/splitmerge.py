import cv2 as cv
import numpy as np

img=cv.imread('tim.jpg')
cv.imshow('tim',img)

blank=np.zeros(img.shape[:2],dtype='uint8')



b,g,r= cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)
green=cv.merge([blank,g,blank])
cv.imshow('green',green)
red=cv.merge([blank,blank,r])
cv.imshow('red',red)

merge= cv.merge([b,g,r])
cv.imshow('merge',merge)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


cv.waitKey(0)