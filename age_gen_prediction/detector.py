import cv2
from deepface import DeepFace

img_path = "test.jpg"

img = cv2.imread(img_path)

response = DeepFace.analyze(img, actions=("age", "gender"))
print(response)