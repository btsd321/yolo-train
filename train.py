from ultralytics import YOLO
from PIL import Image
import datetime
import random
import torch
import sys

if __name__ == '__main__':
    # Load a model
    model = YOLO("yolo11n-seg.yaml")  # build a new model from YAML
    model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolo11n-seg.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

    print(torch.version.cuda)# 查看cuda版本
    # Train the model
    if(torch.cuda.is_available()):
        print("GPU found, count: ", torch.cuda.device_count())  # 输出可用的GPU数量
        results = model.train(
            data="custom_path.yaml", 
            epochs=30, # 训练轮数
            imgsz=640,  # 输入图像尺寸
            device=0,   # 使用第0块GPU进行训练
        )
    else:
        sys.exit("No GPU found, please use CPU for training")
        device = torch.device("cpu")
        print("CPU")
        results = model.train(
            data="custom_path.yaml", 
            epochs=30, # 训练轮数
            imgsz=640,  # 输入图像尺寸
            device="cpu",   # 使用CPU进行训练
        )
        
    # 对单张图片进行推理并可视化结果
    results = model.predict("D:\\Project\\RobotMaster\\yolo-train\\dataset\\images\\test\\20250326_132435_7GKAFKiu.jpg", visualize=True)

    # 显示图片
    print(results)

    model.eval()

    model.export(format="onnx")  # 导出ONNX格式模型