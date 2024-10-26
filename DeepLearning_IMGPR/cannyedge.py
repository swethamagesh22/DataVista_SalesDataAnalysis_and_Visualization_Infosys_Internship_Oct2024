import cv2

img = cv2.imread('/Users/swetha/Desktop/springboard/images/ad3f69afb6b7571d90f225d87bb45315.jpg', 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
