import cv2

videoUrl = "/Users/hujiayu/Desktop/WeChatSight15.mp4"
cap = cv2.VideoCapture(videoUrl)

while( cap.isOpened() ):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('capture', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
