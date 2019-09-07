import cv2
import numpy as np

img = cv2.imread("2.jpg")

kernel = np.array([[-1,-1,-1],[-1,9.7,-1],[-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Image Sharpening", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()


