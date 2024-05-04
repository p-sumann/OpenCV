import cv2 as cv

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)
    
    resized_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
    return resized_frame

capture = cv.VideoCapture(f'Resources\Videos\dog.mp4')

while True:
    
    isTrue, frame = capture.read()
    
    resized_frame = rescale_frame(frame)
    
    cv.imshow(winname='Video', mat=frame)
    cv.imshow(winname='Resized Video', mat=resized_frame)
    
    
    if cv.waitKey(20) and 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
