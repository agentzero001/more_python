import cv2
import numpy as np


image = cv2.imread('captured_image.jpg')
image_array = np.array(image)

cv2.imshow('Image', image_array)

cv2.waitKey(0)
cv2.destroyAllWindows()