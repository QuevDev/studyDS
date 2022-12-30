import cv2 as cv

img = cv.imread('./photos/menu.jpg')

#convirtiendo imagen en escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#desenfoque gaussiano
blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)

#cascada perimetral
canny = cv.Canny(img,125,200) 

#dilatando la imagen
dilated  = cv.dilate(canny,(7,7),iterations=3)

#eroding 
eroded = cv.erode(dilated, (7,7),iterations=4)

#recorte 
coppred = img[100:200,200:400]


cv.imshow('blur', coppred)


cv.waitKey(0)
