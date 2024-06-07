import cv2
img = cv2.imread('surya.jpg', 1)
print(img)
cv2.imshow('surya.jpg', img)
cv2.imwrite('new.jpg', img)
cv2.waitKey(0)
cv2.destroyAllwindows()
