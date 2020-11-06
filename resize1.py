#Tokai University Confidential

import os
import cv2
import glob
i = 0
for filename in os.listdir("./trainB") :
	print("./trainB" + filename)
	tA = cv2.imread("./trainB/" + filename)
    
	print('Original Dimensions tA : ',tA.shape)
	
	scale_percent = 20 # percent of original size
	#width = int(img.shape[1] * scale_percent / 100)
	#height = int(img.shape[0] * scale_percent / 100)
	width=600
	height=400
	dim = (width, height)
	# resize image
	resizedA = cv2.resize(tA, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions tA : ',resizedA.shape)

	dstA = "normal%05d.png" % (i)
	cv2.imwrite(dstA, resizedA, [cv2.IMWRITE_JPEG_QUALITY, 100])
	#os.rename("./testB/" + filename, dst) 
	i += 1
