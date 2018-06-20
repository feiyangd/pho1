# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:23:09 2018

@author: haiyi
"""

import numpy as np
import cv2
from pylab import *
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\\windows\\fonts\\SimSun.ttc",size = 14)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('img1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imwrite('aaa65.jpg',img)
"""
fig = plt.figure()
subplot(121)
plt.gray()
namedWindow("enhanced",0)
imshow(img)
title(u'彩色图', fontproperties= font)
axis('off')
"""
cv2.namedWindow("img",0)
#cv2.cvResizeWindow("img", 500, 500)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
