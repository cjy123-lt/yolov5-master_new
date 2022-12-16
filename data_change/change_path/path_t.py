# import xml.dom.minidom
# import os
#
# path = r'E:\parcel_data\dataset\huangyu\黄钰\annotation'  # xml文件存放路径
# sv_path = r'E:\parcel_data\dataset\huangyu_change'  # 修改后的xml文件存放路径
# files = os.listdir(path)
# cnt = 1
#
# for xmlFile in files:
#     dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
#     root = dom.documentElement  # 得到文档元素对象
#     item = root.getElementsByTagName('path')  # 获取path这一node名字及相关属性值
#     for i in item:
#         i.firstChild.data = 'C:\\Users\\Desktop\\' + str(cnt).zfill(6) + '.jpg'  # xml文件对应的图片路径
#
#     with open(os.path.join(sv_path, xmlFile), 'w') as fh:
#         dom.writexml(fh)
#     cnt += 1

import xml.dom.minidom
import os

path = r'F:\pycharm\pycharm project\yolov5\VOCdevkit\陆小康\annotation'  # xml文件存放路径
sv_path = r'F:\pycharm\pycharm project\yolov5\VOCdevkit\陆小康\ch_annotation'  # 修改后的xml文件存放路径
files = os.listdir(path)
cnt = 1  ##从1开始计数，如果要在前面+0，用zfill函数

for xmlFile in files:
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
    root = dom.documentElement  # 得到文档元素对象
    item = root.getElementsByTagName('path')  # 获取path这一node名字及相关属性值
    item2 = root.getElementsByTagName('folder')  # 获取path这一node名字及相关属性值
    print(item)
    for i in item:
        i.firstChild.data = 'C:\\Users\\83543\\JPEGImages'+'glass' + str(cnt) + '.jpg'  # xml文件对应的图片路径

    for i in item2:
        i.firstChild.data = 'glass' ##folder
    with open(os.path.join(sv_path, xmlFile), 'w') as fh:
        dom.writexml(fh)
    cnt += 1


