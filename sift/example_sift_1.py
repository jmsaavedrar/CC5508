import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)          # queryImage
img2 = cv2.imread('../images/sift/scene.png',cv2.IMREAD_GRAYSCALE) # trainImage

#img1 = cv2.imread('../images/stitching/book.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
#img2 = cv2.imread('../images/stitching/books.png',cv2.IMREAD_GRAYSCALE) # trainImage
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
for mm in matches:
    print('{} {}'.format(kp1[mm.queryIdx].pt, kp2[mm.trainIdx].pt))
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags =2)
 
plt.imshow(img3)
plt.show()