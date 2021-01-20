import cv2

cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
#Resolution: 640 x 480
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
r, frame = cam.read()
print('Resolution: ' + str(frame.shape[1]) + ' x ' + str(frame.shape[0]))

while True:
    r, frame = cam.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) ==ord('q'):
        print("Beende Kamera!")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()