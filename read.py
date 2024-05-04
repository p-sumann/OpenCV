import cv2 as cv

vidoes = r"Resources/Videos/"
images = r"Resources/Photos/"

img = cv.imread(f'{images}cat.jpg')

# cv.imshow(winname='Cat',mat=img)
cv.waitKey(0)


capture = cv.VideoCapture(f'{vidoes}dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Dog',frame)
    
    if cv.waitKey(0) and 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()