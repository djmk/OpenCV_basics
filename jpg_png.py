#Program to convert jpg file to png file

import os
import cv2

for filename in os.listdir("./source_folder") :
	print("./source_folder" + filename)
	tA = cv2.imread("./source_folder/" + filename)
    
	print('Original Dimensions tA : ',tA.shape)

	width=600
	height=400
	dim = (width, height)
	# resize image
	resizedA = cv2.resize(tA, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions tA : ',resizedA.shape)

	dstA = "./destination_folder/" + filename[:-3] + "png"
	cv2.imwrite(dstA, resizedA, [cv2.IMWRITE_JPEG_QUALITY, 100])
	
