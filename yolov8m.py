import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

model=YOLO('yolov8m.pt')

result= model.track(source=0, show=True, persist=True)