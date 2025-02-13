from ultralytics import YOLO
import cv2
import time

# Initialize YOLO model
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")

# Start webcam
cap = cv2.VideoCapture(0)

# Load class labels
class_labels = model.names

# Run detection loop
while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Perform detection
    results = model(frame)

    # Check if any detections are present
    if 'labels' in results[0]:
        # Extract and print class labels
        for label, conf, *box in zip(results[0]['labels'], results[0]['scores'], results[0]['boxes']):
            class_label = class_labels[int(label)]
            print('Detected:', class_label)

            # Use class_label to control the LEDs
            # Add your code here to control LEDs based on class_label

        # Display webcam preview with bounding boxes
        frame = model.show()[0]

    # Display the frame
    cv2.imshow("Webcam Preview", frame)

    # Wait for 5 seconds
    time.sleep(5)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
