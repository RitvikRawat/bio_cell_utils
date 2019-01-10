import cv2
import numpy as np
import math
'''
1. Find no of circles for all possible radii and store in list
2. From list get r_min and r_max
3. Remove overlapping circles st the smaller of two overlapping circles survives
4. Display all circles that are left
5. Display the count of the circles
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

def get_no_circ(img, r):
	img = cv2.medianBlur(img,5)
	img = cv2.bilateralFilter(img,9,75,75)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=r,maxRadius=r)
	if circles is not None:
		return len(circles[0,:])
	else:
		return 0

def get_min_r(no_of_cicr_list):
	r_min = 1
	for i in range(len(no_of_cicr_list)):
		if no_of_cicr_list[i] != 0:
			r_min = i+1
			break
	return r_min

def get_max_r(no_of_cicr_list):
	r_max = int(math.sqrt(x**2 + y**2))
	for r in range(len(no_of_cicr_list)-1, -1, -1):
		if no_of_cicr_list[r] != 0:
			r_max = r+1
			break
	return r_max

def get_no_circ_list(img, l, r):
	no_of_cicr_list = []
	for r in range(l, r):
		x = get_no_circ(img, r)
		no_of_cicr_list.append(x)
	return no_of_cicr_list

path_to_read = '/home/raw/Downloads/growth_study/20.8.18/PI/WT/5f_1.tif'
# path_to_read = 'sample_images/2b.tif'
img = cv2.imread(path_to_read, cv2.IMREAD_GRAYSCALE)
x, y = img.shape

# ideally : int(math.sqrt(x**2 + y**2))
# but here we use a smaller max limit
no_of_cicr_list = get_no_circ_list(img, 1, int(min(x, y)/4))
r_min = get_min_r(no_of_cicr_list)
r_max = get_max_r(no_of_cicr_list)
print r_min, r_max


cimg, detected_circ_no = get_circles_img(img, r_min, r_max)
cv2.imshow('detected circles = ' + str(detected_circ_no), cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
