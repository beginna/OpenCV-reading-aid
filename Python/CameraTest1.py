import cv2

print("Hello World!")
print("Starte Kamera!")

#1. Create an object. Zero for external camera
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)
a=0

while True:
    a = a + 1

    #3 check frame
    check, frame = video.read()

    print(check)
    print(frame) #representing image

    #show frame
    cv2.imshow("Capturing", frame)

    #cv2.waitKey(0)
    key=cv2.waitKey(1)

    if key == ord('q'):
        break
print(a)

#2. Shutdown
video.release
cv2.destroyAllWindows