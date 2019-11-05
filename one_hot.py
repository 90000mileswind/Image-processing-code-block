import numpy as np

#写一个one_hot函数,接收列表，返回one_hot编码
def one_hot(list_num):
    list_onehot = []
    for i in list_num:
        zero_onehot = [0]*10 # 这里是10个类别所以建立10个元素的全零列表
        zero_onehot[i] = 1
        list_onehot.append(zero_onehot)
    return list_onehot

list_num = [1,3,8,0]
N = one_hot(list_num)
print(N)
