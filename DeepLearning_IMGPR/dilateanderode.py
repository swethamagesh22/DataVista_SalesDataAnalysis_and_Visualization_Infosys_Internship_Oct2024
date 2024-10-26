import cv2
import numpy as np

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg', 0)
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Dilated Image', dilation)
cv2.imshow('Eroded Image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()