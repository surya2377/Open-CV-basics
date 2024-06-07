import cv2
cap = cv2.VideoCapture('video.mp4')
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video from File', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video from Webcam', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()