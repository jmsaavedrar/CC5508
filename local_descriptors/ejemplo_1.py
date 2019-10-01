#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 11:39:28 2018

@author: jsaavedr
"""

import cv2
import numpy as np


img = cv2.imread('../images/stitching/caso_3/3a.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create(nOctaveLayers=6, sigma = 1.6)
kp = sift.detect(gray)
kp, des = sift.compute(gray, kp)


img_2 = cv2.imread('../images/stitching/caso_3/3b.jpg')
gray_2= cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
kp_2 = sift.detect(gray_2)
kp_2, des_2 = sift.compute(gray_2, kp_2)

    
matcher=cv2.BFMatcher()
matches = matcher.knnMatch(des,des_2, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.8*n.distance:
        good.append(m)

##Calculando homografía para afinar correspondencias
if len(good)>4:    
    src_pts = np.float32([ kp[m.queryIdx].pt for m in good ]).reshape(-1,2)
    dst_pts = np.float32([ kp_2[m.trainIdx].pt for m in good ]).reshape(-1,2)
    
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 2.0)
    matchesMask = mask.ravel().tolist()
else:
    matchesMask = None

#Aquí, matchesMask contiene las correspondencias
img3 = cv2.drawMatches(img,kp,img_2,kp_2, good, None, flags=2, matchesMask=matchesMask)

cv2.imshow("matches", img3)
cv2.waitKey()