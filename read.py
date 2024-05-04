import cv2 as cv

vidoes = r"Resources/Videos/"
images = r"Resources/Photos/"

img = cv.imread(f'{images}cat.jpg')

cv.imshow(winname='Cat',mat=img)
cv.waitKey(0)

vid = cv.imread(f'{vidoes}dog.mp4')