from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Load a pretrained YOLOv8n model
model = YOLO('C:/1206_aac_train/dataset/runs/detect/train4/weights/best.pt')

# Use the model
result = model.train(data="coco128.yaml", epochs= 200)  #train the model

#train 12 is 100 from sctrach, 14 is 70 from 13, 15 is 100 from 14, train is 100 from 15
#current: 100+70+100+100

#train 2: with conveyer dataset, 66 epochs
#train 3: +30
#train 4: +30
#train 5:+200
