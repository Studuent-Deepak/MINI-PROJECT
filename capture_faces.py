import cv2
import os

name = input("Enter student name: ")

path = "dataset/" + name

if not os.path.exists(path):
    os.makedirs(path)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Capture Faces", frame)

    img_path = f"{path}/{count}.jpg"
    cv2.imwrite(img_path, frame)

    count += 1

    if count == 20:
        break

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Images captured successfully!")