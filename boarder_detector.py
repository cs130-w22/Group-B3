import cv2
import numpy as np
import imutils

# Read the original image

img = cv2.imread('img4.jpeg')

# Display original image

cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
print(edges)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)


cv2.destroyAllWindows()

def bad_contour2(c):
    min_x = np.Inf
    min_y = np.Inf
    max_x = np.NINF
    max_y = np.NINF
    min_dim = 50
    
    for c_list in c:
        for x,y in c_list:
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
    
    x_len = max_x - min_x
    y_len = max_y - min_y
    
    peri = cv2.arcLength(c,True)
    
    area = x_len * y_len
    
    retval = True
    if (peri < 50) or area < 500 or (x_len < min_dim and y_len < min_dim): 
        retval = False
    return retval

cnts = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
mask = np.ones(img.shape[:2], dtype="uint8") * 255

for c in cnts:
    if bad_contour2(c):
        cv2.drawContours(mask, [c], -1, 0, -1)
        
image = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

thresh = 50
ret,thresh_img = cv2.threshold(edges, thresh, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = np.zeros(img.shape)
cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
cv2.imwrite('contours.png',img_contours)