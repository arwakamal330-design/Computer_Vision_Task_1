import cv2
import numpy as np
import matplotlib.pyplot as plt

images = ["img_1.jpg","img_2.jpg","img_3.jpg"]

for image in images :

    img = cv2.imread(image)


    if img is None :
        raise FileNotFoundError
    
    else:

        ##===============information of images (name,shape,type,total_pixels,center_pixel)====================

        print (image)
        print ("shape: ",img.shape)
        print ("type : ",img.dtype)

        h,w,n = img.shape

        print ("total pixels : ", h*w)

        Cx = w//2
        cy = h//2

        print ("BGR center pixels : ", img[Cx,cy])


        ##================================== the float32 conversion =====================================

        img_f = img.astype(np.float32)/255.0

        h,w,n = img_f.shape

        cx =w//2
        cy = h//2

        print ("Float pixel center : ",img_f[cx,cy])

        result = np.clip (img_f,0.0,1.0)

        img_back = (result *255).astype(np.uint8)

        name = image.split(".")[0]

        cv2.imwrite (name + "_output.jpg",img_back)

        print ("\n")

        ##====================================== Splicing Channels =====================================

        B = img [:,:,0]
        G = img [:,:,1]
        R = img [:,:,2]


        fig , ax = plt.subplots(1,3,figsize=(10,6))

        ax[0].imshow(B,cmap='gray')
        ax[0].set_title("Blue")

        ax[1].imshow(G,cmap='gray')
        ax[1].set_title("Green")

        ax[2].imshow(R,cmap='gray')
        ax[2].set_title("red")

        plt.savefig (name + "_gray_output.jpg")

        plt.show()

  
