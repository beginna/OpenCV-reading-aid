import cv2


cam = cv2.VideoCapture(1)
scale=1
while True:
    ret_val, image = cam.read()

    #get the webcam size
    height, width, channels = image.shape

    #prepare the crop
    centerX,centerY=int(height/2),int(width/2)
    radiusX,radiusY= int(height/(2*scale)),int(width/(2*scale))

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = image[minX:maxX, minY:maxY]
    resized_cropped = cv2.resize(cropped, (width, height)) 

    cv2.imshow('my webcam', resized_cropped)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
 
    if cv2.waitKey(1) ==ord('1'): 
        scale = 1  #1x
        #cv2.imshow('my webcam', resized_cropped)

    if cv2.waitKey(1) ==ord('2'): 
        scale = 2  #?
        cv2.imshow('my webcam', resized_cropped)

    if cv2.waitKey(1) ==ord('3'): 
        scale = 3  #?
        cv2.imshow('my webcam', resized_cropped)
        

cv2.destroyAllWindows()