import cv2 as cv 

img = cv.imread('./photos/menu.jpg')

cv.imshow('normal img',img)

#BRG to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray img',gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV img',hsv)

#BRG to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitKey(0)
