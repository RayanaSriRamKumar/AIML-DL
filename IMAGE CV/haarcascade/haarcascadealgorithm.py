import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in faces:
        # Calculate center and radius for circle
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        cv2.circle(img, center, radius, (255, 255, 0), 2)
    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10)
    if key == 27:  # ESC key
        break

cam.release()
cv2.destroyAllWindows()
