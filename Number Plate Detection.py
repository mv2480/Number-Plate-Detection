import cv2
####
frameWidth = 640
frameHeight = 480
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
####`
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        if w*h > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            imgR = img[y:y+h, x:x+w]
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(255,0,0), 2)
            cv2.imshow('Result', img)
            cv2.imshow('Croped',imgR)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break