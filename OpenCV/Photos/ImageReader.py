def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)





import cv2 as cv #importing the cv library

img=cv.imread('Car.jpg')

img=rescaleFrame(img,1.5)
cv.imshow('jerry',img)


cv.waitKey(0)
