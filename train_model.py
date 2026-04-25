import face_recognition
import os
import pickle
import cv2

dataset_path = "dataset"

known_encodings = []
known_names = []

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        print("Processing:", image_path)

        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

data = {
    "encodings": known_encodings,
    "names": known_names
}

os.makedirs("trainer", exist_ok=True)

with open("trainer/encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("Training complete. Encodings saved.")