import cv2
cap = cv2.VideoCapture('video.mp4')
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
target_width = 1280
target_height = 720

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (target_width, target_height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for (x, y, w, h) in face.detectMultiScale(gray, 1.1, 5):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('FaceCam9', frame)
    if cv2.waitKey(2) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
