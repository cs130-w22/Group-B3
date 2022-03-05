from PIL import Image
import cv2

def get_crops(image, boxes):
    crops = []
    for box in boxes:
        x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
        cv_crop = image[x1:x2, y1:y2]
        cv_crop = cv2.cvtColor(cv_crop, cv2.COLOR_BGR2RGB)
        crop = Image.fromarray(cv_crop)
        crops.append(crop)
    return crops


