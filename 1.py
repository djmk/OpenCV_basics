import os
import cv2
import glob
i = 0
print(len(os.listdir("./after")))
#print(os.listdir("./real"))
print(len(os.listdir("./before")))
#print(os.listdir("./aiphotec"))
aiphotec_list = os.listdir("./after")
real_list = os.listdir("./before")
#for file0 in os.listdir("./real"):
print(aiphotec_list)
#print(real_list)
for file1 in aiphotec_list:
    if file1 not in real_list:
        print(file1)
        os.remove("./after/" + file1)
            



