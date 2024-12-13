import cv2

#打开摄像头，并展示
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

#释放摄像头
cap.release()
cv2.destroyAllWindows()