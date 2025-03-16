import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model = YOLO("path/to/yolov8n.pt")
    model.export(format='onnx', simplify=True, opset=13)