import cv2 as cv

#img = cv.imread('./photos')

#1)Rending videos
#2) Resizing 
capture = cv.VideoCapture(0)


def rescaleFrame(frame, scale=0.5):
    #img,videos,camaraweb
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA)

#camaraweb
def resLiveVideo(width, height):
    capture.set(3,width)
    capture.set(4,height)




while(capture.isOpened()):
    #aca preguntamos con un booleano si el valor
    #se leyo bien 
    ret,frame = capture.read() 
    cam_gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    #usamos la funcion de rescalar el video
    frame_resized = rescaleFrame(cam_gray)
    
    cv.imshow('webCam',frame_resized) 

    if(cv.waitKey(1) & 0xFF == ord('s')):
        break


        
capture.release()
cv.destroyAllWindows()
