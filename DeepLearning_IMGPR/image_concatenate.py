import cv2
import numpy as np

img1 = cv2.imread('/Users/swetha/Desktop/springboard/images/dog.jpg')
img2 = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg')

img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

h_concat = np.hstack((img1, img2))
v_concat = np.vstack((img1, img2))

cv2.imshow('Horizontal Concatenation', h_concat)
cv2.imshow('Vertical Concatenation', v_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()