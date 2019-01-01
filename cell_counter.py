import cv2
import numpy as np

'''
approaches find a suitable r_min and r_max and only
show circles that are in between these limits
How to find r_min and r_max ???
'''

def get_circles_img(img):
	img = cv2.medianBlur(img,5)
	# img = cv2.GaussianBlur(img,(5,5),0)
	img = cv2.bilateralFilter(img,9,75,75)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=10,maxRadius=60)
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
	    # draw the outer circle
	    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	return cimg

def check_radius(img, r):
	img = cv2.medianBlur(img,5)
	img = cv2.bilateralFilter(img,9,75,75)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=r,maxRadius=r)
	if circles is not None:
		return True
	else:
		return False


img = cv2.imread('sample_images/2b.tif', cv2.IMREAD_GRAYSCALE)
print img.shape

# for radius in range(1,200):
# 	print check_radius(img, radius)

cimg = get_circles_img(img)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()




# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
