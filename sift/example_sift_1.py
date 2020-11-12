import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/stitching/book.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
img2 = cv2.imread('../images/stitching/books.png',cv2.IMREAD_GRAYSCALE) # trainImage
#img1 = cv2.imread('../images/stitching/caso_1/1a.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
#img2 = cv2.imread('../images/stitching/caso_1/1b.jpg',cv2.IMREAD_GRAYSCALE) # trainImage

#find the keypoints and descriptors with SIFT
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:  x.distance)

# #Apply ratio test
# good = []
# for m,n in matches:
#     print("{} {}".format(m.distance,n.distance))
#     if m.distance < 0.75*n.distance:
#         good.append([m])
#  
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:40], None, flags =2 )
 
plt.imshow(img3)
plt.show()