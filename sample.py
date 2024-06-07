import cv2
image = cv2.imread('surya.jpg')
cv2.rectangle(image,(50,100),(200,500),(20,50,100),5)
cv2.imshow(image)
