#Removing the missing files from the two folders

import os
import cv2

print(len(os.listdir("./folder1")))
print(len(os.listdir("./folder2")))

folder1_list = os.listdir("./folder1")
folder2_list = os.listdir("./folder2")

print(folder1_list)
print(folder2_list)

for file1 in folder2_list :
    if file1 not in folder1_list:
        print(file1)
        os.remove("./folder2/" + file1)
            



