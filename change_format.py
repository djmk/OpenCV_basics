#Example of Changing the files format for pre-processing (jpg or png)

import os
import cv2

print(len(os.listdir("./folder")))

pngs = os.listdir('./folder')
print(pngs)
for j in pngs:
    #img = cv2.imread(j)
    #cv2.imwrite(j[:-3] + 'jpg', img)
    os.rename("./folder/" + j, "./folder/" + j[:-3] + 'jpg')

print(os.listdir("./folder"))
            



