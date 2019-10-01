#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:50:08 2018

@author: jsaavedr

This examples requires openCV
"""
import cv2 
import numpy as np

img = cv2.imread('../images/stitching/caso_1/1b.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray)
print("n_kp: {}".format(len(kp)))
#kp, des = sift.compute(gray, kp)
cv2.drawKeypoints(gray,kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("img1", img)

cv2.waitKey()
