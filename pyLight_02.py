'''
Author: Tie Hu
Date: 2018/08/18
Description: Python Code to Find Edge
'''
import cv2 # import opencv 
import PyQt5 # import PyQt 
import numpy as np # import numpy
from matplotlib import pyplot as plt # import matplotlib

img =cv2.imread('IMG_Street.jpg') 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
px = img[100,100]
print(px)
print (img.shape)
print (img.dtype)
print (img.size)
plate = img[280:340,330:390]
img[273:333,100:160] = plate
cv2.imwrite('street.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

