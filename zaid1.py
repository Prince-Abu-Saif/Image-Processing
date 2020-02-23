import cv2

face_cascade = cv2.CascadeClassifier(r'cars.xml')
#li=['a.jpg','b.jpg','d.jpg']
#for i in li:

video = cv2.VideoCapture(r'car.mp4')
while True:
    check,frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)

    for x,y,w,h in faces:
        rect=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    print(faces)

    cv2.imshow("my image",frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
video.release()