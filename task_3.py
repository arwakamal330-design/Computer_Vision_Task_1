import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread ("img_1.jpg")

if img is None :
    raise FileNotFoundError
else:
    bgr = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    ycrcb = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

    fig ,ax = plt.subplots(1,5,figsize=(12,6))

    ax[0].imshow (bgr)
    ax[0].set_title("original");ax[0].axis('off')

    ax[1].imshow (grayscale,cmap='gray')
    ax[1].set_title("gray");ax[1].axis('off')

    ax[2].imshow(hsv)
    ax[2].set_title("hsv");ax[2].axis('off')

    ax[3].imshow(lab)
    ax[3].set_title("LAB");ax[3].axis('off')

    ax[4].imshow(ycrcb)
    ax[4].set_title("YCrCb");ax[4].axis('off')

    plt.show()

    h, w = img.shape[:2]
    cy = h // 2
    cx = w // 2

    print("BGR   :", img[cy, cx])
    print("Gray  :", grayscale[cy, cx])
    print("HSV   :", hsv[cy, cx])
    print("LAB   :", lab[cy, cx])
    print("YCrCb :", ycrcb[cy, cx])

    lower_yellow = np.array([15, 50, 50])
    upper_yellow = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    result = cv2.bitwise_and(img, img, mask=mask)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(1, 3, figsize=(12, 5))

    ax[0].imshow(img_rgb)
    ax[0].set_title("Original")

    ax[1].imshow(mask, cmap="gray")
    ax[1].set_title("Binary Mask")

    ax[2].imshow(result_rgb)
    ax[2].set_title("Segmented Result")

    for a in ax:
        a.axis("off")

    plt.tight_layout()
    plt.show()

    
    
