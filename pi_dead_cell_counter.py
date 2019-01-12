import cv2
import numpy as np
import math
'''
Read this
https://stackoverflow.com/questions/42206042/ellipse-detection-in-opencv-python
'''

def get_circles_img(img, r_min, r_max):
	orig_img = img
	img = cv2.medianBlur(img,5)
	# img = cv2.GaussianBlur(img,(5,5),0)
	img = cv2.bilateralFilter(img,9,75,75)
	cimg = cv2.cvtColor(orig_img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=r_min,maxRadius=r_max)
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
	    # draw the outer circle
	    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	return cimg, len(circles[0,:])

def get_bitmap(img):
	x, y, _ = img.shape
	thresh = np.zeros((3, x, y))
	bitmap_img = np.zeros((x, y))
	for i in range(0,3):
		ret,thresh[i] = cv2.threshold(img[:,:,i],60,255,cv2.THRESH_BINARY)
		if np.array_equal(thresh[i], np.zeros((x, y))):
			print "Empty"
		else:
			print "Not Empty"
			# bitmap_img = thresh[i]
			bitmap_img = img[:,:,i]
	return bitmap_img

def get_labelled_fluorescent_img(path_to_read):
	img = cv2.imread(path_to_read, cv2.IMREAD_UNCHANGED)
	x, y, _ = img.shape
	bitmap_img = get_bitmap(img)
	# blur_bitmap = cv2.blur(bitmap_img,(5,5))
	blur_bitmap = cv2.GaussianBlur(bitmap_img,(7,7),0)
	# blur_bitmap = np.array(blur_bitmap * 255, dtype = np.uint8)

	r_min = 10
	r_max = 50
	print r_min, r_max
	cimg, detected_circ_no = get_circles_img(blur_bitmap, r_min, r_max)
	return cimg, detected_circ_no

	# cv2.imshow('Filtered Image', blur_bitmap)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


# path_to_read = '/home/raw/Downloads/growth_study/24.8.18/M/7b.tif'
path_to_read = 'sample_images/3f.tif'
cimg, detected_circ_no = get_labelled_fluorescent_img(path_to_read)


cv2.imshow('detected circles = ' + str(detected_circ_no), cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
