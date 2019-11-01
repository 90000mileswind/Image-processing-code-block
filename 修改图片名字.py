import os
import re
import sys

path = r"F:\Image data\水表数字识别数据集\voc格式标注_ymoon"


def renameall(path):
    fileList = os.listdir(path)  # 待修改文件夹
    print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
    currentpath = os.getcwd()  # 得到进程当前工作目录
    os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
    num = 1  # 名称变量
    Nstr = '00000'
    for fileName in fileList:  # 遍历文件夹中所有文件
        i = len(str(num))
        os.rename(fileName, (Nstr[:-i] + str(num) + '.' + fileName[-3:]))  # 文件重新命名
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件


renameall(path)
