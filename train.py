from ultralytics import YOLO
from PIL import Image
import datetime
import random
import torch
import sys
import onnx

if __name__ == '__main__':
    # Load a model
    # model = YOLO("yolo11n-pose.yaml")  # build a new model from YAML
    # model = YOLO("yolo11n-pose.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolo11n-pose.yaml").load("yolo11n-pose.pt")  # build from YAML and transfer weights

    print(torch.version.cuda)# 查看cuda版本
    # Train the model
    if(torch.cuda.is_available()):
        print("GPU found, count: ", torch.cuda.device_count())  # 输出可用的GPU数量
        results = model.train(
            data="custom_path.yaml", 
            epochs=100, # 训练轮数
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
    results = model(["dataset/images/test/20250326_215453_7D43hmCl.jpg"])  # return a list of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        # result.show()  # display to screen
        result.save(filename="result.jpg")  # save to disk
        # 打印 boxes, masks, keypoints, probs, obb 信息
        print("boxes: ", boxes)
        print("masks: ", masks)
        print("keypoints: ", keypoints)
        print("probs: ", probs)
        print("obb: ", obb)

    model.eval()

    model.export(format="onnx")  # 导出ONNX格式模型