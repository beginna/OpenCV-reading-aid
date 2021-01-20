import cv2

print("Hello World!")
print("Starte Kamera!")

cap = cv2.VideoCapture(1)
capwidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
capheight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#print(capheight,"x", capwidth)
print(capwidth,"x", capheight)


#cap.set(3, 400)
#cap.set(4, 600)
while True:
        sucess, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) ==ord('q'):
            print("Beende Kamera!")
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()