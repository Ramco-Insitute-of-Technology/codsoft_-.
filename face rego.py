import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('sample.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import face_recognition
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)

if len(unknown_encoding) > 0:
    results = face_recognition.compare_faces([known_encoding], unknown_encoding[0])
    
    if results[0]:
        print("Face recognized: It's a match!")
    else:
        print("Face not recognized: It's a different person.")
else:
    print("No face found in the unknown image.")
