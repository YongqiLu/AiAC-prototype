from ultralytics import YOLO
import pandas as pd

# Load YOLO model
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")

# Perform prediction on the webcam feed with stream=True
results = model.predict(source="0", stream=True)  # accepts all formats

# Define your classes and corresponding text responses
class_mapping = {
    0: "aac",
    1: "nail",
    2: "wood"
}

# Process each frame in the stream
for r in results:
    # If there are detections in the frame
    if r.xyxy[0] is not None:
        # Convert the results to a Pandas DataFrame
        df = pd.DataFrame(r.xyxy[0], columns=['x_min', 'y_min', 'x_max', 'y_max', 'confidence', 'class'])

        # Filter out low-confidence detections
        df = df[df['confidence'] > 0.5]

        # Extract the detected classes from results
        detected_classes = df['class'].astype(int).tolist()

        # Define the text responses based on the detected classes
        text_response = ""

        if 0 in detected_classes:
            text_response += "G"
        if 1 in detected_classes:
            text_response += "R"
        if 2 in detected_classes:
            text_response += "Y"

        # Print the final text response
        if text_response:
            print(f"Text Response: {text_response}")
        else:
            print("Text Response: 0")

    # Optionally, you can print the original results as well
    print(r)
