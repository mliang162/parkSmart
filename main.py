import cv2

mask = './mask_crop.png'
video_path = './videosample/carpark.mp4'
ret = True

cap = cv2.VideoCapture(video_path)
connected_components = cv2.connectedComponents(mask, 4, cv2.CV2_32S)

while ret:
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    if cv2.waitkey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
