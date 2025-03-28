from ultralytics import YOLO
from PIL import Image
import datetime
import random
import torch
import sys
import onnx


# 对单张图片进行推理并可视化结果
model = YOLO("runs/pose/train/weights/best.pt")  # build from YAML and transfer weights
results = model(["dataset/images/test/20250327_175217_rMC5cmNa.jpg"])  # return a list of Results objects

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