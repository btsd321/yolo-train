# 将给定文件内内的yolo-seg标签文件批量转换为yolo-pose标签文件
# 原yolo-seg标签格式为：
# <object-class> <x1> <y1> <x2> <y2> <x3> <y3> <x4> <y4>
# 转换后的yolo-pose标签格式为：
# <object-class> <x> <y> <width> <height> <px1> <py1> <px2> <py2> <px3> <py3> <px4> <py4>
# 其中<x> = min(x1, x2, x3, x4) - diff
# <y> = min(y1, y2, y3, y4) - diff
# <width> = max(x1, x2, x3, x4) - min(x1, x2, x3, x4) + diff * 2
# <height> = max(y1, y2, y3, y4) - min(y1, y2, y3, y4) + diff * 2
# <px1> = <x1> ; <py1> = <y1>
# <px2> = <x2> ; <py2> = <y2>
# <px3> = <x3> ; <py3> = <y3>
# <px4> = <x4> ; <py4> = <y4>


import os
import cv2
import numpy as np

input_file_path = 'D:/Project/RobotMaster/yolo-train/origin_data/labels'
output_file_path = 'D:/Project/RobotMaster/yolo-train/origin_data/labels_pose'

diff = 0.0001
all_file_count = 0
convert_file_count = 0
error_file_count = 0

if not os.path.exists(output_file_path):
    os.makedirs(output_file_path)

for file in os.listdir(input_file_path):
    if file.endswith('.txt'):
        file_path = os.path.join(input_file_path, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
        with open(os.path.join(output_file_path, file), 'w') as f:
            all_file_count += 1
            line_num = 0
            for line in lines:
                line_num += 1
                line = line.strip()
                if line:
                    try:
                        object_class, x1, y1, x2, y2, x3, y3, x4, y4 = line.split()
                    except ValueError:
                        print('Error:', line)
                        print('Error File:', file)
                        error_file_count += 1
                        continue
                    x = min(float(x1), float(x2), float(x3), float(x4)) - diff
                    if x < 0:
                        x = 0
                    y = min(float(y1), float(y2), float(y3), float(y4)) - diff
                    if y < 0:
                        y = 0
                    width = max(float(x1), float(x2), float(x3), float(x4)) - x + diff * 2
                    height = max(float(y1), float(y2), float(y3), float(y4)) - y + diff * 2
                    if x + width > 1:
                        width = 1 - x
                    if y + height > 1:
                        height = 1 - y
                    f.write(object_class + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(height) + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + x3 + ' ' + y3 + ' ' + x4 + ' ' + y4 + '\n')
                    print(object_class, x, y, width, height, x1, y1, x2, y2, x3, y3, x4, y4)
                    print('Done:', file)
                    
            if line_num != 1:
                print('Error File:', file)
                error_file_count += 1
            else:
                convert_file_count += 1
                    
print('All files have been converted,!')
print('All file count:', all_file_count)
print('Convert file count:', convert_file_count)
print('Error file count:', error_file_count)

