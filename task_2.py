import cv2
import numpy as np
import matplotlib.pyplot as plt

images = ["img_1.jpg","img_2.jpg","img_3.jpg"]

for image in images :

    img = cv2.imread(image)


    if img is None :
        raise FileNotFoundError
    
    else:

        ##=============== information of images (name,shape,type,total_pixels,center_pixel) ====================

        print (image)
        print ("shape: ",img.shape)
        print ("type : ",img.dtype)

        h,w,n = img.shape

        print ("total pixels : ", h*w)

        cx = w//2
        cy = h//2

        center = img [cy,cx]

        print ("B : ", center[0])
        print ("B : ", center[1])
        print ("B : ", center[2])

        ##==================================== Draw Circle ======================================

        cy = h//2
        cx = w//2
        r = min(h,w)//10
        y,x = np.ogrid[:h,:w]
        mask_c = abs((y-cy)**2+(x-cx)**2-r**2)<=50
        img[mask_c]= [255,255,255]
        cv2.imshow ("image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        ##================================== the float32 conversion =====================================

        img_f = img.astype(np.float32)/255.0

        h,w,n = img_f.shape

        cx =w//2
        cy = h//2

        print ("Float pixel center : ",img_f[cy,cx])

        result = np.clip (img_f,0.0,1.0)

        img_back = (result *255).astype(np.uint8)

        print ("\n")

        ##====================== splicing Channels ===========================

        B , G , R = img[:,:,0],img[:,:,1],img[:,:,2]
        fig , axis = plt.subplots (1,3,figsize=(12,6))
        for ax,ch,name in zip (axis,[B,G,R],['Blue','Green','Red']):
            ax.imshow(ch,cmap='gray')
            ax.set_title (name)
            ax.axis('off')
        plt.tight_layout()
        name = image.split(".")[0]
        plt.savefig(name + "gray_output.jpg")
        plt.show()

