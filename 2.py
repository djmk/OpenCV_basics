import os
import cv2
import glob
i = 0
print(len(os.listdir("./after")))

pngs = os.listdir('./after')
print(pngs)
for j in pngs:
    #img = cv2.imread(j)
    #cv2.imwrite(j[:-3] + 'jpg', img)
    os.rename("./after/" + j, "./after/" + j[:-3] + 'jpg')

print(os.listdir("./after"))
            



