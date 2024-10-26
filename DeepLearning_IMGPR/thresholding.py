import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg', 0)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()