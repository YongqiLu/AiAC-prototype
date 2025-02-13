import serial
from ultralytics import YOLO
import cv2
import time

# loading the YOLO model from the directory
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")

# Connect to Arduino
arduino_connection = serial.Serial('COM3', 9600)
time.sleep(2)  # Allow time for Arduino to initialize

# Control LEDs based on detection results
def control_leds(aac_detected, nail_detected, wood_detected):
    led_command = '0'  # Default: Turn off all LEDs

    if aac_detected and not nail_detected and not wood_detected:
        led_command = 'G'  # Green LED
    elif aac_detected and nail_detected and not wood_detected:
        led_command = 'R'  # Red LED
    elif aac_detected and not nail_detected and wood_detected:
        led_command = 'Y'  # Yellow LED
    elif nail_detected and wood_detected:
        led_command = 'A'  # Both red and yellow LEDs

    # Print debugging information
    print("Sending LED command:", led_command)

    # Send the command to Arduino with a delimiter
    arduino_connection.write(f"{led_command}\n".encode())

# Main loop
frames_processed = 0
while True:
    # Capture webcam input and perform YOLO detection
    start_time = time.time()
    results = model.predict(source="0", show=True)
    elapsed_time = time.time() - start_time

    # Close the webcam preview window after 5 seconds or press any key to continue
    if elapsed_time >= 5 or cv2.waitKey(1) & 0xFF != 255:
        cv2.destroyAllWindows()

    # Process YOLO results and control LEDs
    aac_detected = False
    nail_detected = False
    wood_detected = False

    for result in results.xyxy[0]:
        label = int(result[5])  # Assuming class information is in the last column

        if label == 0:  # ACC class
            aac_detected = True
        elif label == 1:  # nail class
            nail_detected = True
        elif label == 2:  # wood class
            wood_detected = True

    # Control LEDs based on detection results
    control_leds(aac_detected, nail_detected, wood_detected)

    # Batch processing: Send commands every N frames
    frames_processed += 1
    if frames_processed >= 10:
        arduino_connection.write(b'0\n')  # Ensure LEDs are off during processing
        control_leds(aac_detected, nail_detected, wood_detected)
        frames_processed = 0

    # Introduce delay to control frame rate
    time.sleep(5.0)  # 1 frame every 5 seconds
