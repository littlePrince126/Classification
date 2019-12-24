# _*_coding:utf-8
#!/usr/bin/env python
# 引入“咖啡”
import caffe

import numpy as np

# 使输出的参数完全显示
# 若没有这一句，因为参数太多，中间会以省略号“……”的形式代替
np.set_printoptions(threshold='nan')

# 均值文件
MEAN_FILE = 'mean.binaryproto'
# 保存参数的文件
means_txt = 'means.txt'
mf = open(means_txt, 'w')

# 将均值文件读入blob中
mean_blob = caffe.proto.caffe_pb2.BlobProto()
mean_blob.ParseFromString(open(MEAN_FILE, 'rb').read())

# 将均值blob转为numpy.array
mean_npy = caffe.io.blobproto_to_array(mean_blob)
# 均值参数是多维数组，为了方便输出，转为单列数组
mean_npy.shape = (-1, 1)
for m in mean_npy:
    # 写参数
    mf.write('%ff, ' % m)

mf.close