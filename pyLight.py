'''
Author: Tie Hu
Date: 2018/08/18
Description: Python Code to Find Edge
'''
import cv2
import PyQt5
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread('IMG_Street.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
px = img[100,100]
print(px)
print (img.shape)
print (img.dtype)
print (img.size)
cv2.imwrite('street.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

