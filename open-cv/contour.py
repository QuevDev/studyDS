import cv2 as cv 
import numpy as np 



img = cv.imread('./photos/menu.jpg')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

blank = np.zeros(img.shape, dtype='uint8')

ret, tresh = cv.threshold(gray,50,255,cv.THRESH_BINARY)

cv.imshow('img' , tresh)

contours, hierachies = cv.findContours(tresh, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

#dibujando un contorno en un lienzo blanco
cv.drawContours(blank,contours,-1,(0,255,0),1 )
cv.imshow('blank', blank)

cv.waitKey(0)
