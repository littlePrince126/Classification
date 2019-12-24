#!/bin/sh
if ! test -f models/bvlc_alexnet/train_val.prototxt ;then
	echo "error: example/MobileNetSSD_train.prototxt does not exist."
	echo "please use the gen_model.sh to generate your own model."
        exit 1
fi
#mkdir -p snapshot
#  /home/little_prince/caffe/build/tools/caffe train -solver="models/bvlc_alexnet/#solver.prototxt" \

sudo GLOG_logtostderr=0 GLOG_log_dir=/home/little_prince/SSD_disk/caffe_practise/models/bvlc_alexnet/logs  /home/little_prince/caffe/build/tools/caffe train -solver /home/little_prince/SSD_disk/caffe_practise/models/bvlc_alexnet/solver.prototxt 
#-model="models/ResNet-18/resnet-18.caffemodel" \
#-gpu 0

#-snapshot="/home/little_prince/MobileNet-SSD/snapshot/mobilenet_iter_6285.solverstate" \
#-model="/home/little_prince/MobileNet-SSD/mobilenet_iter_73000.caffemodel" \
