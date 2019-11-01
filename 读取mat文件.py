import scipy.io as scio

path = r'F:\Image data\数字字母数据集2000\trainCharBound.mat'
matdata = scio.loadmat(path)
print(matdata)
