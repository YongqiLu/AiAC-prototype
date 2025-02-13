from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO("best.pt")

# Define path to the image file
#source = 'C:/1206_aac_train/dataset/runs/detect/train12/image.jpg'

# Run inference on an image
results = model('C:/1206_aac_train/dataset/val/images/IMG_8085.jpg')  # results list

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('C:/1206_aac_train/dataset/0testrun/IMG_8085_1.jpg')  # save image

