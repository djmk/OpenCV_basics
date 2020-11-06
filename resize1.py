#Tokai University Confidential

import os
import cv2

for filename in os.listdir("./before") :
	print("./before" + filename)
	tA = cv2.imread("./before/" + filename)
    
	print('Original Dimensions tA : ',tA.shape)

	width=600
	height=400
	dim = (width, height)
	# resize image
	resizedA = cv2.resize(tA, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions tA : ',resizedA.shape)

	dstA = "./before1/" + filename[:-3] + "png"
	cv2.imwrite(dstA, resizedA, [cv2.IMWRITE_JPEG_QUALITY, 100])
	
