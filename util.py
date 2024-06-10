import pickle
from skimage.transform import resize
import numpy as np
import cv2

EMPTY = True
NOT_EMPTY = False
MODEL = pickle.load(open("model.p", "rb"))

def emptiness(spot_bgr):
    flat_data = []
    resized_img = resize(spot_bgr, (15, 15, 3))
    flat_data.append(resized_img.flatten())
    flat_data = np.array(flat_data)
    y_output = MODEL.predict(flat_data)
    
    if y_output == 0:
        return EMPTY
    else:
        return NOT_EMPTY
    
def get_parking_spots_bboxes(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components
    
    slots = []
    coefficient = 1
    for i in range(1, totalLabels):
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coefficient)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coefficient)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coefficient)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coefficient)
        
        slots.append([x1, y1, w, h])
        
    return slots
