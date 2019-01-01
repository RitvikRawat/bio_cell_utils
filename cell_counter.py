import cv2
import numpy as mp
img = cv2.imread('sample_images/1b.tif')
print img.shape
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()