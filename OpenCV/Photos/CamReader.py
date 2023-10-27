import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


capture= cv.VideoCapture(0)
#0 for webcam , give the path to read a video file

while True:
    isTrue,frame=capture.read()
    frame=rescaleFrame(frame,0.5)
    cv.imshow('Video',frame)
    
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
