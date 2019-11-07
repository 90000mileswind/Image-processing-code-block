import random
import sys
from PIL import Image
import tensorflow as tf
import numpy as np
import os

RANDOM_SEED = 21         # 给定随机数种子




def get_image_shape(filename1):
    """ filename图片文件地址，返回形状
        用tensorflow也可用Pillow和NumPy更简单一点吧
    """
    image = Image.open(filename1)
    image = np.asarray(image, np.uint8)
    shape = np.array(image.shape, np.int32)
    return shape, image.tobytes()# convert image to raw data bytes in the array.

def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _process_image(directory, name):
    # 1. 构造图像路径
    i_img_class = int(name[3:6])  # 图片属于哪个类别，截取文件名字符串转化为数字就是其类别
    i_len = len(str(i_img_class))
    filename = os.path.join(directory[:-i_len] + str(i_img_class), name) # 拼接图片文件路径

    # 2. 加载数据
    shape, image_data = get_image_shape(filename)  # 获取图片文件形状
    label = i_img_class  # 标签是数字,先转换成字符串

    return image_data, label, shape

def _convert_to_example(image_data, label, shape):
    # 这个格式要求和pascalvoc_common.py中定义的keys_to_features的格式一致。
    # 构建Example对象
    example = tf.train.Example(features=tf.train.Features(feature={
        'label': _int64_feature(label),
        'image': _bytes_feature(image_data),
        'h': _int64_feature(shape[0]),
        'w': _int64_feature(shape[1])
    }))
    return example

def _add_to_tfrecord(dataset_dir, name, tfrecord_writer):
    # 1. 处理图像，获取得到这个图像中的相关信息,dataset_dir="/test4/Imagedata/num_img/Sample001",name是“img001-00034.png”
    image_data, label, shape = _process_image(dataset_dir, name)

    # 2. 将数据转换为TensorFlow Example的形式
    example = _convert_to_example(image_data, label, shape)

    # 3. 数据输出
    tfrecord_writer.write(example.SerializeToString())

# 1. TFRecord生成
def writer(dataset_dir, output_dir, shuffling=False):
    """
    测试写数据形成TFRecord文件
    """
    if not tf.io.gfile.exists(dataset_dir):
        tf.gfile.MakeDirs(dataset_dir)
    if not tf.io.gfile.exists(output_dir):
        tf.gfile.MakeDirs(output_dir)
    # 获取所有图片名字生成图片文件路径和标签
    img_names = []
    #  图片放在10个文件夹中，得分别取出来,全部放到img_names列表中
    for i_file in range(1, 11):
        i_len = len(str(i_file))
        dataset_dir0 = dataset_dir[:-i_len] + str(i_file)
        img_names.extend(os.listdir(dataset_dir0))
    if shuffling:
        # 如果需要shuffle，那么进行随机数种子给定后，进行shuffle操作
        random.seed(RANDOM_SEED)
        random.shuffle(img_names)

    #划分训练、测试、验证
    train_test_val = [0.7, 0.2, 0.1]
    train_num = int(train_test_val[0]*len(img_names))
    test_num = int((train_test_val[0] + train_test_val[1])*len(img_names))
    val_num = len(img_names)

    # 4. 遍历处理所有的xml文件
    i = 0
    while i < val_num:  # 等于len(img_names),就是整个图片名字列表的长度
        if i < train_num:
            SAMPLES_PER_FILES = train_num
            name = 'train'
        elif i < test_num:
            SAMPLES_PER_FILES = test_num
            name = 'test'
        else:
            SAMPLES_PER_FILES = val_num
            name = 'val'

        # a. 获取TFRecord对应的文件路径
        tf_filename = os.path.join(output_dir, '%s.tfrecord' % (name))
        # b. 构造TFRecord数据输出对象
        with tf.io.TFRecordWriter(tf_filename) as tfrecord_writer:
            while i < SAMPLES_PER_FILES:
                sys.stdout.write('\r>> Converting image %d/%d' % (i + 1, len(img_names)))
                sys.stdout.flush()

                # 1. 获取得到当前处理的文件名称
                img_name = img_names[i]
                # 3. 数据处理
                _add_to_tfrecord(dataset_dir, img_name, tfrecord_writer)
                i += 1


dataset_dir = "/test4/Imagedata/num_img/Sample001"  # 图片数据所在文件夹
output_dir = "./data/ftrecord"  # 输出文件夹
writer(dataset_dir, output_dir, shuffling=True)