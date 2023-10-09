#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2


img=cv2.imread('C:/Users/AK/Documents/shapes.png',0)
#img =cv2.resize(img,(500,600))


# In[ ]:


ret,thresh = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
cnts,heir=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

area1=[]
for c in cnts:
   
    
   # M = cv2.moments(c)
    #print("M==",M)
    #cX = int(M["m10"] / M["m00"])
    #cY = int(M["m01"] / M["m00"])
    
    area=cv2.contourArea(c)
    area1.append(area)
        
    
    
    if area<1000:
        
        ep=0.1*cv2.arcLength(c,True)
        data=cv2.approxPolyDP(c,ep,True)
        
        
        hull=cv2.convexHull(data)
        
        
        x,y,w,h=cv2.boundingRect(hull)
        
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(122,80,120),4)
        
        
        cv2.drawContours(img, [c], -1, (50, 100, 50), 2)
        #cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
        #cv2.putText(img, "center", (cX - 20, cY - 20),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        
        
        
cv2.imshow("original===",img)
#cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()     

