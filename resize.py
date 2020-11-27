#For changing the size(height and width) of image files using OpenCV.
# Initialize the width and height variables with the desired height and width of the image

import os
import cv2

for filename in os.listdir("./imagefolder") :
	print("./imagefolder" + filename)
	tA = cv2.imread("./imagefolder/" + filename)
    
	print('Original Dimensions tA : ',tA.shape)
	width=600
	height=600
	dim = (width, height)
	# resize image
	resizedA = cv2.resize(tA, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions tA : ',resizedA.shape)
 
	dstA ="./destination folder/" + filename
	cv2.imwrite(dstA, resizedA)
