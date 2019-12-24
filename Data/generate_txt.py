# _*_coding:utf-8
#LoadAbsoluteName.py
#提取指定文件夹下对应格式文件的绝对路径
import os

labels=["face","smoking"]

def ListFilesToTxt(dir,file,wildcard,recursion,NeedAbsolutePath):
    exts = wildcard.split(" ")
    print(dir)
    files = os.listdir(dir)
   #print(files)
    for name in files:
        tk=0
        for label in labels:
            if dir.find(label)>=0:
                break
            else:
                tk+=1
        fullname = os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion,NeedAbsolutePath)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    if NeedAbsolutePath:
                        if fullname.find("face")>=0:
                            tk1=0
                        else:
                            tk1=1
                        file.write(fullname+" "+str(tk1)+"\n")
                    else:
                        file.write(name+"\n")
                    break

def Test():
    dir = r"/home/little_prince/SSD_disk/caffe_practise/Data/val/"
    wildcard = ".jpg"
    outfile="val.txt"
    file = open(outfile,"w")
    if not file:
        print("can not open the file")
    ListFilesToTxt(dir,file,wildcard,1,1)

    file.close()

def Train():
    dir = r"/home/little_prince/SSD_disk/caffe_practise/Data/train/img"
    wildcard = ".jpg"
    outfile="train.txt"
    file = open(outfile,"w")
    if not file:
        print("can not open the file")
    ListFilesToTxt(dir,file,wildcard,1,1)

    file.close()
    
if __name__ == "__main__":
    #Test()
    Train()