# import numpy as np  
# import sys,os  
# import cv2
# import caffe


# net_file= '/home/little_prince/SSD_disk/caffe_practise/models/bvlc_alexnet/deploy.prototxt'
# caffe_model='/home/little_prince/SSD_disk/caffe_practise/snapshot/alexenet_iter_450000.caffemodel'
# test_dir = "./test_img/"

# if not os.path.exists(caffe_model):
#     print(caffe_model + " does not exist")
#     exit()
# if not os.path.exists(net_file):
#     print(net_file + " does not exist")
#     exit()
# net = caffe.Net(net_file,caffe_model,caffe.TEST)  

# CLASSES = ('face',
#            )


# def preprocess(src):
#     img = cv2.resize(src, (227,227))
# #    img = img - 127.5
#     img=img-127.5
#     img = img * 0.007843
#     return img



# def detect(imgfile):
#     porigimg = cv2.imread(imgfile)
#     size=porigimg.shape
#     width=size[1]
#     height=size[0]
   
#     if(height>2000):
#       #  origimg=preprocess(cv2.resize(porigimg,(int(height*1),int(width*0.1))))
#         origimg=porigimg
#     else:
#         origimg=porigimg
# #    origimg = cv2.resize(imga, (1333, 1000))

#     img = preprocess(origimg)
    
#     img = img.astype(np.float32)
#     img = img.transpose((2, 0, 1))

#     net.blobs['data'].data[...] = img
#     out = net.forward()  
#     prob= net.blobs['prob'].data[0].flatten()
  
#     #print(out)
#     print(prob)
   
#     return True

# for f in os.listdir(test_dir):
# #    if detect("/home/little_prince/caffe/data/VOCdevkit/VOC2007/JPEGImages" + "/" + "31937.jpg") == False:
#     # if detect("./test_img/" + "/" + "1.jpg") == False:
#     #    break
#    print(f)
#    detect("./test_img/"+f)



import caffe
import sys
import numpy as np
 
caffe_root='/home/caffe/'
sys.path.insert(0,caffe_root+'python')
 
caffe.set_mode_cpu()

deploy='/home/little_prince/SSD_disk/caffe_practise/models/bvlc_alexnet/deploy.prototxt'
caffe_model='/home/little_prince/SSD_disk/caffe_practise/snapshot/alexenet_iter_450000.caffemodel'
img='./test_img/timg.jpg'
labels_name='/home/little_prince/SSD_disk/caffe_practise/Data/label.txt'
mean_file='/home/little_prince/SSD_disk/caffe_practise/Data/mean_alex.npy'
 
net=caffe.Net(deploy,caffe_model,caffe.TEST)
 
transformer=caffe.io.Transformer({'data':net.blobs['data'].data.shape})
transformer.set_transpose('data',(2,0,1))
transformer.set_mean('data',np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data',255)
transformer.set_channel_swap('data',(2,1,0))
 
image=caffe.io.load_image(img)
net.blobs['data'].data[...]=transformer.preprocess('data',image)
 
out=net.forward()
labels=np.loadtxt(labels_name,str,delimiter='\t')
 
prob=net.blobs['prob'].data[0].flatten()
top_k=net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
for i in np.arange(top_k.size):
    print top_k[i],labels[top_k[i]],prob[top_k[i]]
