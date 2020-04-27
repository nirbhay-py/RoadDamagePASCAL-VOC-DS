import os
for filename in os.listdir(os.getcwd()):
	if filename.endswith(".xml"):
		# num = (fin.split(".")[0]).split("_")[1]
		f = open(filename,'r')
		filedata = f.read()
		f.close()

		newdata = filedata.replace("/Users/nirbhaysingh/Desktop/objectDetection/images/","/Users/arjunpandey/Desktop/CVProject/TensorFlow/workspace/training_demo/images/Images/")

		f = open(filename,'w')
		f.write(newdata)
		f.close()
