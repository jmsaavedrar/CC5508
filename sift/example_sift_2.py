import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/stitching/fontana_1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../images/stitching/fontana_2.jpg', cv2.IMREAD_GRAYSCALE)
#img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)          
#img2 = cv2.imread('../images/sift/scene.png',cv2.IMREAD_GRAYSCALE)
#img1 = cv2.imread('../images/stitching/book.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
#img2 = cv2.imread('../images/stitching/books.png',cv2.IMREAD_GRAYSCALE) # trainImage 

#find the keypoints and descriptors with SIFT
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
print(len(matches))
print(matches)
good = []
for  m,n in matches:
    if m.distance < 0.8*n.distance:
        good.append(m)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags =2)
 
plt.imshow(img3)
plt.show()