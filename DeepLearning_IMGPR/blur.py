import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg')
blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
