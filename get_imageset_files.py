import os
import random
trainfile=open("train.txt","w")
valfile=open("val.txt","w")
testfile=open("test.txt","w")
trainvalfile=open("trainval.txt","w")

jpg_name=[i for i in range(33866)]
random.shuffle(jpg_name)

for i in range(0,3000):
	trainfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")

for i in range(3500,5500):
	trainfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")

for i in range(6000,11000):
	trainfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")
for i in range(6000,11000):
	trainfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
# for i in range(12000,17000):
# 	trainfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
# for i in range(18000,23000):
# 	trainfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
# for i in range(24000,29000):
# 	trainfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
for i in range(30000,33866):
	trainfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")


for i in range(3000,3500):
	valfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")

for i in range(5500,6000):
	valfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")
# for i in range(11000,12000):
# 	valfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
# for i in range(23000,24000):
# 	valfile.write(str(jpg_name[i])+"\n")
# 	trainvalfile.write(str(jpg_name[i])+"\n")
for i in range(29000,30000):
	valfile.write(str(jpg_name[i])+"\n")
	trainvalfile.write(str(jpg_name[i])+"\n")
	

for i in range(2000,4000):
	testfile.write(str(jpg_name[i])+"\n")


#for i in range(20,30):
#	testfile.write(str(jpg_name[i])+"\n")




trainfile.close()
valfile.close()
testfile.close()
trainvalfile.close()
