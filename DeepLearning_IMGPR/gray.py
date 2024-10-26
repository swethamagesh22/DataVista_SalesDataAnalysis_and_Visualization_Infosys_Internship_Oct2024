import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()