from ultralytics import YOLO
import serial
import time
import sys

# Load YOLO model
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")
# Open serial port for Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for Arduino to initialize

# Label commands mapping
label_commands = {
    'aac': 'G', 'nails': 'R', 'wood': 'Y', 'aac_nail_wood': 'A', 'none': '0'
}

while True:
    try:
        # Get YOLO predictions
        results = model.predict(source="0")
        detected_labels = [item['label'] for item in results.xyxy[0].numpy()]

        # Determine command
        command = '0'  # Default command
        if 'aac' in detected_labels and not 'nails' in detected_labels and not 'wood' in detected_labels:
            command = label_commands['aac']
        elif 'nails' in detected_labels:
            command = label_commands['nails']
        elif 'wood' in detected_labels:
            command = label_commands['wood']
        elif 'nails' in detected_labels and 'wood' in detected_labels:
            command = label_commands['aac_nail_wood']
        else:
            command = label_commands['none']
        # Add other conditions as required

        # Debugging output
        print(f"Detected Labels: {detected_labels}")
        print(f"Sending command to Arduino: {command}")
        sys.stdout.flush()

        # Send command to Arduino
        arduino.write(command.encode())

    except Exception as e:
        print(f"Error: {e}")
        sys.stdout.flush()

    time.sleep(5)  # Wait before next iteration