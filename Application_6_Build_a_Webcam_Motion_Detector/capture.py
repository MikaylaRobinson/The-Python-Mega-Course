import cv2, time
from datetime import datetime
import pandas as pd

first_frame = None

# Keep a list of the times where the status changes 
status_list = [None, None]
times = []
df = pd.DataFrame(columns=["Start", "End"])
video = cv2.VideoCapture(0)

a = 0
while True:
    # Collecting first frame with no motion and then getting the gray version
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21, 21), 0)

    # Delaying the capture of the base frame because of distorted image when camera first turns on
    if (first_frame is None) and (a < 20):
        a += 1
        continue
    elif first_frame is None:
        first_frame = gray
        continue

    # Finding the difference between the first frame and the current frame
    delta_frame = cv2.absdiff(first_frame, gray)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Looking for contours bigger than this, and once it finds it, change the status
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue 
        status = 1

        # Adding rectangles around the objects in the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 3)

    # Tracking the times that the status changes (When something enters or exits the frame)
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    # Display all of the frames 
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    # How to end the capture
    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start":times[i],"End":times[i + 1]}, ignore_index = True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows