import os
import xml.etree.ElementTree as ET

def changesku(inputpath):
    listdir = os.listdir(inputpath)
    for file in listdir:
        if file.endswith('xml'):
            file = os.path.join(inputpath,file)
            tree = ET.parse(file)
            root = tree.getroot()
            folder = root.findall('folder')
            filename = root.findall('filename')
            path = root.findall('path')
            folder[0].text = 'voc2007watermeter'
            filename[0].text = filename[0].text[:-3] + 'jpg'
            path[0].text = 'F:\Imagedata\\voc2007watermeter\JPEGImages\\' + filename[0].text
            tree.write(file, encoding='utf-8')  # 写进原始的xml文件，不然修改就无效，‘encoding = “utf - 8”’避免原始xml
        else:
            pass

if __name__ == '__main__':
    inputpath = r'F:\Imagedata\voc2007watermeter\Annotations'#这是xml文件的文件夹的绝对地址
    changesku(inputpath)

