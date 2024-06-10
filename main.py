import cv2
import util

# Read the mask image
mask_path = './mask_crop.png'
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

if mask is None:
    raise FileNotFoundError(f"Mask image not found at {mask_path}")

# Ensure the mask is a binary image (only 0 and 255 values)
_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

video_path = './samples/carpark.mp4'
cap = cv2.VideoCapture(video_path)
ret = True

# Use the mask in connectedComponentsWithStats
connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
spots = util.get_parking_spots_bboxes(connected_components)
print(spots[0])

while ret:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
