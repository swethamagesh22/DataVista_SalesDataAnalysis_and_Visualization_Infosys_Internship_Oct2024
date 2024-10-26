import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg')
cropped = img[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()