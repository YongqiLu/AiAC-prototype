from ultralytics import YOLO

model = YOLO("C:/1206_aac_train/dataset/runs/detect/train/weights/best.pt")

results = model.predict(source ="0", show = True) # accpets all formats
print(results)