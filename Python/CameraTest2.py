import cv2

print("Hello World!")
print("Starte Kamera!")

cap = cv2.VideoCapture(0)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

#change_res(640, 480)
change_res(320, 240)

while True:
    sucess, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) ==ord('q'):
        print("Beende Kamera!")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()