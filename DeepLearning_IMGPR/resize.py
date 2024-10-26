import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg')
resized = cv2.resize(img, (300, 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()