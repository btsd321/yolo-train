# 将图片和标注数据按比例切分为 训练集和测试集
import shutil
import random
import os
import argparse

# 检查文件夹是否存在，如果不存在则创建
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main(image_dir, txt_dir, save_dir):
    # 创建保存数据集的文件夹
    mkdir(save_dir)
    images_dir = os.path.join(save_dir, 'images')  # 创建images文件夹路径
    labels_dir = os.path.join(save_dir, 'labels')  # 创建labels文件夹路径

    img_train_path = os.path.join(images_dir, 'train')  # 创建训练图片文件夹路径
    img_test_path = os.path.join(images_dir, 'test')  # 创建测试图片文件夹路径
    img_val_path = os.path.join(images_dir, 'val')  # 创建验证图片文件夹路径

    label_train_path = os.path.join(labels_dir, 'train')  # 创建训练标注文件文件夹路径
    label_test_path = os.path.join(labels_dir, 'test')  # 创建测试标注文件文件夹路径
    label_val_path = os.path.join(labels_dir, 'val')  # 创建验证标注文件文件夹路径

    # 创建相应的文件夹
    mkdir(images_dir)
    mkdir(labels_dir)
    mkdir(img_train_path)
    mkdir(img_test_path)
    mkdir(img_val_path)
    mkdir(label_train_path)
    mkdir(label_test_path)
    mkdir(label_val_path)

    # 数据集划分比例，训练集85%，验证集15%，测试集0%，按需修改
    train_percent = 0.85
    val_percent = 0.15
    test_percent = 0  # 注意：测试集比例为0，所有数据会分配到训练集和验证集

    total_txt = os.listdir(txt_dir)  # 获取所有标注文件的文件名
    num_txt = len(total_txt)  # 计算标注文件的数量
    list_all_txt = range(num_txt)  # 生成所有标注文件索引的列表

    num_train = int(num_txt * train_percent)  # 计算训练集的数量
    num_val = int(num_txt * val_percent)  # 计算验证集的数量
    num_test = num_txt - num_train - num_val  # 计算测试集的数量（此处应为0）

    train = random.sample(list_all_txt, num_train)  # 随机选择num_train个索引作为训练集
    # 在全部数据集中取出train，剩下的就是val_test
    val_test = [i for i in list_all_txt if not i in train]
    # 再从val_test取出num_val个元素，val_test剩下的元素就是test
    val = random.sample(val_test, num_val)

    # 打印训练集、验证集和测试集的数量
    print("训练集数目：{}, 验证集数目：{},测试集数目：{}".format(len(train), len(val), len(val_test) - len(val)))

    # 遍历所有标注文件的索引
    for i in list_all_txt:
        name = total_txt[i][:-4]  # 获取文件名，去掉扩展名.txt

        srcImage = os.path.join(image_dir, name + '.jpg')  # 源图片路径
        srcLabel = os.path.join(txt_dir, name + '.txt')  # 源标注文件路径

        if i in train:
            # 如果是训练集，复制图片和标注文件到训练集文件夹
            dst_train_Image = os.path.join(img_train_path, name + '.jpg')
            dst_train_Label = os.path.join(label_train_path, name + '.txt')
            shutil.copyfile(srcImage, dst_train_Image)
            shutil.copyfile(srcLabel, dst_train_Label)
        elif i in val:
            # 如果是验证集，复制图片和标注文件到验证集文件夹
            dst_val_Image = os.path.join(img_val_path, name + '.jpg')
            dst_val_Label = os.path.join(label_val_path, name + '.txt')
            shutil.copyfile(srcImage, dst_val_Image)
            shutil.copyfile(srcLabel, dst_val_Label)
        else:
            # 如果是测试集，复制图片和标注文件到测试集文件夹
            dst_test_Image = os.path.join(img_test_path, name + '.jpg')
            dst_test_Label = os.path.join(label_test_path, name + '.txt')  # 修正了这里的一个错误，原本有一个符号错误
            shutil.copyfile(srcImage, dst_test_Image)
            shutil.copyfile(srcLabel, dst_test_Label)

# 如果脚本作为主程序运行，则执行以下代码
if __name__ == '__main__':
    """
    使用命令行参数运行此脚本示例：
    python split_datasets.py --image-dir my_datasets/color_rings/imgs --txt-dir my_datasets/color_rings/txts --save-dir my_datasets/color_rings/train_data
    """
    parser = argparse.ArgumentParser(description='将数据集划分为训练集、验证集和测试集的参数设置')
    parser.add_argument('--image-dir', type=str, default='D:/Project/RobotMaster/yolo-train/images',
                        help='图片路径文件夹')
    parser.add_argument('--txt-dir', type=str, default='D:/Project/RobotMaster/yolo-train/labels',
                        help='标注文件路径文件夹')
    parser.add_argument('--save-dir', default='D:/Project/RobotMaster/yolo-train/dataset', type=str,
                        help='保存划分后数据集的路径文件夹')
    args = parser.parse_args()  # 解析命令行参数
    image_dir = args.image_dir  # 获取图片路径参数
    txt_dir = args.txt_dir  # 获取标注文件路径参数
    save_dir = args.save_dir  # 获取保存路径参数

    main(image_dir, txt_dir, save_dir)  # 调用main函数进行数据集的划分
