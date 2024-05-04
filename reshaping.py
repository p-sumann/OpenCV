import cv2 as cv

def rescale_frame(frame, scale=0.75):
    
    # this one works for imaegs, vidoes and live vidoes
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)
    
    resized_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
    return resized_frame

def change_res(width, height):
    # this one only works with live video data
    cv.set(3, width)
    cv.set(4, height)

capture = cv.VideoCapture(f'Resources\Photos\cat_large.jpg')

while True:
    
    isTrue, frame = capture.read()
    
    resized_frame = rescale_frame(frame,scale=0.25)

    if cv.waitKey(0) and 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
