# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:46:02 2020

@author: shrikant
"""

import cv2 


img = cv2.imread('lena.jpg',1)

cv2.imshow('Image', img)
k = cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("lena_copy.png",img)
    cv2.destroyAllWindows()

