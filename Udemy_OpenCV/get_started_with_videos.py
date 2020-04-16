# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:33:56 2020

@author: shrikant
"""

import cv2

cap= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('data/output.avi',fourcc,20.00, (640,480))

while (True):
    ret, frame=cap.read()
     
    if ret== True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)
        """For color video
        cv2.imshow(frame', frame) """
        
       
        
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('frame', gray)
        
        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break
   
cap.release()
out.release()
cv2.destroyAllWindows()
          