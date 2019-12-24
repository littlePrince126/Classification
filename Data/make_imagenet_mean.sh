#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/little_prince/SSD_disk/caffe_practise/Data
DATA=/home/little_prince/SSD_disk/caffe_practise/Data
TOOLS=/home/little_prince/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/train_lmdb_alex \
$DATA/train_alex.binaryproto

echo "Done."
