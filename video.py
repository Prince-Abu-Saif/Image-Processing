import cv2

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
#li=['a.jpg','b.jpg','d.jpg']
#for i in li:

video = cv2.videoCapture('abcd.mp4',1)
while True:
    check,frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

    for x,y,w,h in faces:
        rect=cv2.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),3)

    print(faces)

    cv2.imshow("my image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    video.release()