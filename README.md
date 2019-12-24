
# Training ResNet18 or AlexNet for classification
By Linfeng

[caffe]("https://github.com/BVLC/caffe") 

Please build caffe

## 1.Make Dataset for classification
```
Data
#train
##face
##smoking
#val
##face
##smoking
```
## 2.Convert Dataset to lmdb

cd Data
python LoadAbsoluteName.py #get train.txt and val.txt

cd ..
./create_imagenet.sh #get lmdb Dataset

## 3.Get mean.binaryproto and mean.npy

sudo ~/PATH-TO-CAFFE/caffe/build/tools/compute_image_mean ./Data/train_lmdb #get the mean.binaryproto

sudo python convert_mean.py mean.binaryproto mean.npy #get mean.npy

## 4.training 
Please modfiy the path of your dataset and hyperparameters of solver.prototxt
run  train.sh for ResNet-18
run  train_alex.sh for Alex-Net
