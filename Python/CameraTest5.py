import cv2


cam = cv2.VideoCapture(1)
scale=1
while True:
    ret_val, image = cam.read()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,  
                'ESC: beenden',  
                (10, 30),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)

    cv2.putText(image,  
                '1, 2, 3: Zoom',  
                (10, 60),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)

    #get the webcam size
    height, width, channels = image.shape

    #prepare the crop
    centerX,centerY=int(height/2),int(width/2)
    radiusX,radiusY= int(height/(2*scale)),int(width/(2*scale))

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = image[minX:maxX, minY:maxY]
    resized_cropped = cv2.resize(cropped, (width, height)) 

    cv2.imshow('Lesehilfe', resized_cropped)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
 
    if cv2.waitKey(1) ==ord('1'): 
        scale = 1  #1x
        #cv2.imshow('my webcam', resized_cropped)

    if cv2.waitKey(1) ==ord('2'): 
        scale = 2  #2x
        #cv2.imshow('my webcam', resized_cropped)

    if cv2.waitKey(1) ==ord('3'): 
        scale = 3  #3x
        #v2.imshow('my webcam', resized_cropped)
        
cam.release()
cv2.destroyAllWindows()