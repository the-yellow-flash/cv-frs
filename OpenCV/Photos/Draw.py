

import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank',blank)

#1. paint the image a certain color
""" blank[:,200:300]=0,0,255  #  row, column =blue,green,red
blank[200:300]=0,255,0 """

cv.rectangle(blank,(100,100),(200,200),(0,0,255),thickness=50)
cv.imshow('Green',blank)
cv.waitKey(0)
