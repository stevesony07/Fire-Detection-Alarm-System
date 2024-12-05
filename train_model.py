!pip install roboflow
!pip install ultralytics

from roboflow import Roboflow
from ultralytics import YOLO

# Initialize Roboflow and download the dataset
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("your_workspace").project("continuous_fire")
version = project.version(6)
dataset = version.download("yolov8")

# Train the model
!yolo task=detect mode=train model=yolov8s.pt data=dataset.location/data.yaml epochs=1 imgsz=640 plots=True

# Validate the model
!yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=dataset.location/data.yaml
