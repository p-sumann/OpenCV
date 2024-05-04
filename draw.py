import cv2 as cv
import numpy

zeros = numpy.zeros([500,500,3], dtype='float64')
img = cv.imread('Resources/Photos/cat.jpg')


# 1. paint an image to certain color
# zeros[:] = 0,255,0


# 2. create a rectangle from an image
cv.rectangle(zeros, (0,0),(img.shape[1]//2,img.shape[0]//2),(0,0,255), thickness=cv.FILLED)
# cv.imshow(winname='Blank', mat=zeros)

# 3. draw a circle 
cv.circle(zeros, (img.shape[1]//2,img.shape[0]//2), 40, (0,250,0),thickness=cv.FILLED)
cv.imshow(winname='Blank', mat=zeros)

cv.waitKey(0)
# cv.imshow(winname='Blank', mat=zeros)
# cv.imshow(winname='Cat', mat=img)




