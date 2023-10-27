import cv2
import numpy as np

#reading the image
image =cv2.imread('tim.jpg')
cv2.imshow('tim',image)

#grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)


#performing edge detection

gradients_sobelx=cv2.Sobel(gray,-1,1,0)
cv2.imshow('sobelx',gradients_sobelx)
gradients_sobely=cv2.Sobel(gray,-1,0,1)
cv2.imshow('sobely',gradients_sobely)
gradients_sobelxy=cv2.addWeighted(gradients_sobelx,0.5,gradients_sobely,0.5,0)
cv2.imshow('sobelx',gradients_sobelxy)
gradients_laplacian=cv2.Laplacian(gray,-1)
cv2.imshow('laplacian',gradients_laplacian)





#bluring the image
blur=cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)

#canny edge 

canny=cv2.Canny(blur,10,80)
cv2.imshow('canny',canny)
cv2.waitKey(0)