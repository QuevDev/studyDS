import cv2 as cv

img = cv.imread('./photos/menu.jpg')
cv.imshow('normal img', img)

cv.waitKey(0)
