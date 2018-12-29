import cv2
import os

images = os.listdir("sample-images")

for files in images:
    img = cv2.imread(os.path.join("sample-images",files))
    resized = cv2.resize(img, (100,100))
    cv2.imwrite("resized"+files, resized)