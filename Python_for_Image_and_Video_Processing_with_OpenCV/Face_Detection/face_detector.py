import cv2

# Using the frontal face cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
gray_version = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Setting detection parameters to only capture the frontal faces in this image
faces = face_cascade.detectMultiScale(gray_version,
scaleFactor = 1.1,
minNeighbors = 5)

# Setting up a rectangle to appear around each detected face
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()