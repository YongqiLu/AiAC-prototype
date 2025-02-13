from ultralytics import YOLO
import serial
import time
import sys

# Load YOLO model
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")

results = model.predict(source="0", stream=True, show = True)

arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for Arduino to initialize

# for each frame
for result in results:
  class_ids = result.boxes.cls.tolist()
  detected_labels = [result.names[int(i)] for i in class_ids]
  print("Detected:", detected_labels)
  #['person', 'person', 'cat']
  #(if 2 person, 1 cat detected in a frame)