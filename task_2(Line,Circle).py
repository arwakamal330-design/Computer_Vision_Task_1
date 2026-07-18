import cv2
import numpy as np

x = 500
y = 500

img = np.zeros((x, y), dtype=np.uint8)

# Draw Line From (50, 50) to (300, 300)

for i in range(50, 301):
    img[i, i] = 150


cx = 100
cy = 100
r = 50

# Draw Circle Circle centered at (100, 100), Circle radius = 50

for y in range(500):
    for x in range(500):
        if abs(((x - cx)**2 + (y - cy)**2) - r**2) <= 50 :
            img[y, x] = 150

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()