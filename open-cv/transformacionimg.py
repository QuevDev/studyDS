import cv2 as cv 
import numpy as np

img = cv.imread('./photos/menu.jpg')
#cv.imshow('img',img)


#translacion 
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> izquierda 
# -y --> arriba
# +y --> abajo
# +x ---> derecha

#Rotacion 
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    print(height,width)
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, height)
    return cv.warpAffine(img,rotMat,dimensions) 
   
#cambiar tamanho 
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)   
cv.imshow('resized',resized)

#flip 
flip = cv.flip(img,0)    
      
translated = translate(img,100,100)
cv.imshow('translated',translated)

rotated = rotate(img,90)
cv.imshow('rotated', rotated)


cv.waitKey(0)

