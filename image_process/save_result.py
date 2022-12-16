import os
import cv2
from openpyxl import Workbook
import pytesseract as tess

def recognize_text(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("binimg", gray)
    ret, binnary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)
    # cv2.imshow("binmg", binnary)
    kerhel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    bin1 = cv2.morphologyEx(binnary, cv2.MORPH_OPEN, kerhel1, iterations=1)
    kerhel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
    bin2 = cv2.morphologyEx(binnary, cv2.MORPH_OPEN, kerhel2, iterations=1)
    # cv2.imshow("binary_img",bin2)
    text = tess.image_to_string(bin2)
    print("识别结果：%s"%text)
    return text

# 创建一个新的工作簿wb
wb = Workbook()
# 使用active获取创建工作簿wb时自动生成的sheet
sheet = wb.active

path = r'E:\parcel_data\yolov5-master_new\runs\detect\exp4\crops\big_number'
for file in os.listdir(path):
    # append的入参要求是list, tuple, range or generator, or a dict
    print(file)
    img = cv2.imread(os.path.join(path,file))
    text = recognize_text(img)
    sheet.append([file,text])

# 工作簿落盘
wb.save(r'E:\parcel_data\yolov5-master_new\image_process\data_save\dataset.xlsx')