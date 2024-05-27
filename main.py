import cv2

ret = True
video_path = './videosample/carpark.mp4'
cap = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    if cv2.waitkey(25) & 0xFF == ord('q'):
        break
cap.release()
