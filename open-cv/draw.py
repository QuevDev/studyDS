import cv2 as cv
import numpy as np

#crear una imagen en blanco

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank', blank)
#img = cv.imread('./photos/menu.jpg')

#dibujar un rectangulo 
cv.rectangle(blank,(10,10),(200,200),(0,255,0),thickness=4)

#dibujar un circulo 
cv.circle(blank,(100,100),40,(255,0,0),thickness=-1)

#dibujar una linea
cv.line(blank,(100,0),(200,200),(0,0,255),thickness=1,lineType=90)

#insertar texto
cv.putText(blank,'Hola mundo',(255,255),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),4,2)

cv.imshow('Rectangle',blank)


#cv.imshow('menu',blank)

cv.waitKey(0)