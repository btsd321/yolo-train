# yolo-train
yolo-train

Epoch: 训练的轮数，即模型已经遍历整个训练数据集的次数。
GPU_mem: 使用的GPU内存。
box_loss: 边界框预测的损失。
seg_loss: 分割预测的损失。
cls_loss: 类别分类的损失。
dfl_loss: 分布式焦点损失（Distributed Focal Loss），用于改进目标检测的稳定性。
Instances: 每个epoch处理的实例（目标）数量。
Size: 输入到模型的图像尺寸。
在每个epoch之后，模型会在验证集上进行评估，并输出以下性能指标：

Class: 评估的类别。
Images: 评估使用的图像数量。
Instances: 评估使用的实例数量。
Box(P): 边界框的精确率（Precision）。
Box(R): 边界框的召回率（Recall）。
mAP50: 交并比大于0.5时的平均精度（Mean Average Precision at IoU > 0.5）。
mAP50-95: 交并比在0.5到0.95之间时的平均精度（Mean Average Precision at IoU > 0.5 to 0.95）。

pip freeze > requirements.txt # 生成依赖包列表
pip install -r requirements.txt # 安装依赖包

# 本项目需要cuda_12.6.3_561.17_windows环境和cudnn8.9.7.29环境，请确保安装正确的环境。