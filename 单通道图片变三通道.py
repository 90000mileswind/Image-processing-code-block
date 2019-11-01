'''
数据集是单通道的灰度图，需要转成三通道后才能喂入SSD模型中。
使用的方法比较简单，将单通道的复制两份强行变成三通道。
'''
import os
import cv2

imgfilepath = r'F:\Imagedata\voc2007watermeter\JPEGImages\\'
total_img = os.listdir(imgfilepath)
print(len(total_img))
#从文件夹中取出文件
for img in total_img:
    # 首先以灰色读取一张照片
    src = cv2.imread(imgfilepath + img, 0)
    # 然后用ctvcolor（）函数，进行图像变换。
    src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(imgfilepath + img, src_RGB)#保存图片替换原图
    print(img, '变换后通道数：{}'.format(src_RGB.shape))

'''
# 首先以灰色读取一张照片
src = cv2.imread(r'F:\Imagedata\voc2007watermeter\JPEGImages\1.jpg', 0)
print(src.shape)

# 然后用ctvcolor（）函数，进行图像变换。
src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
print(src_RGB.shape)

cv2.imwrite(r'F:\Imagedata\voc2007watermeter\JPEGImages\1new_one.jpg',src_RGB)
print('存储成功！！！')
'''


