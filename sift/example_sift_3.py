"""
jsaavedr
Showing SIFT matching and filtering by the best transformation
"""
import cv2
from matplotlib import pyplot as plt
import transform
import numpy as np

#img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)   # queryImage
#img2 = cv2.imread('../images/sift/scene.png',cv2.IMREAD_GRAYSCALE) # trainImage
#img1 = cv2.imread('../images/stitching/fontana_1.jpg', cv2.IMREAD_GRAYSCALE)
#img2 = cv2.imread('../images/stitching/fontana_2.jpg', cv2.IMREAD_GRAYSCALE)
#img1 = cv2.imread('../images/stitching/book.jpg',cv2.IMREAD_GRAYSCALE)   # queryImage
#img2 = cv2.imread('../images/stitching/books.png',cv2.IMREAD_GRAYSCALE) # trainImage
#img1 = cv2.imread('../images/stitching/caso_3/3a.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
#img2 = cv2.imread('../images/stitching/caso_3/3b.jpg',cv2.IMREAD_GRAYSCALE) # trainImage
img1 = cv2.imread('../images/stitching/st1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../images/stitching/st2.jpg', cv2.IMREAD_GRAYSCALE)

#find the keypoints and descriptors with SIFT
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:  x.distance)
matches = matches[:100]
n_matches = len(matches)
#coorespondencias en coordenadas homogeneas
src = np.zeros((3,n_matches), dtype=np.float32)
dst = np.zeros((3,n_matches), dtype=np.float32)
for i in range(n_matches) :
    src[0][i] = kp1[matches[i].queryIdx].pt[0]
    src[1][i] = kp1[matches[i].queryIdx].pt[1]
    src[2][i] = 1
    dst[0][i] = kp2[matches[i].trainIdx].pt[0]
    dst[1][i] = kp2[matches[i].trainIdx].pt[1]
    dst[2][i] = 1
T = transform.estimate_transformation(src, dst, th_dist = 5)
##obtener inliers
points_t = np.matmul(T,src)
points_t = points_t/points_t[2,:]
d_error = np.sqrt(np.sum(np.square(dst[0:2,:] - points_t[0:2,:]), axis = 0))
good = []
for  i,err in enumerate(d_error):
    #print('{} ->  {}'.format(i,err))
    if err <= 5 :
        good.append(matches[i])    
#drawrectangle
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags =2)
draw_box = False
if draw_box :
    src_box = np.ones((3,4), dtype = np.float32)
    src_box[0][0] = 0  
    src_box[1][0] = 0
    
    src_box[0][1] = img1.shape[1]
    src_box[1][1] = 0
    
    src_box[0][2] = img1.shape[1]
    src_box[1][2] = img1.shape[0]
    
    src_box[0][3] = 0
    src_box[1][3] = img1.shape[0]
    
    dst_box = np.matmul(T,src_box)
    dst_box = dst_box/dst_box[2,:]
    dst_box[0,:] = dst_box[0,:] + img1.shape[1]  

    img3 = cv2.line(img3, (src_box[0][0],src_box[1][0]), (src_box[0][1],src_box[1][1]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (src_box[0][1],src_box[1][1]), (src_box[0][2],src_box[1][2]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (src_box[0][2],src_box[1][2]), (src_box[0][3],src_box[1][3]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (src_box[0][3],src_box[1][3]), (src_box[0][0],src_box[1][0]), (255,0,22), thickness = 2 )
     
    img3 = cv2.line(img3, (dst_box[0][0],dst_box[1][0]), (dst_box[0][1],dst_box[1][1]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (dst_box[0][1],dst_box[1][1]), (dst_box[0][2],dst_box[1][2]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (dst_box[0][2],dst_box[1][2]), (dst_box[0][3],dst_box[1][3]), (255,0,22), thickness = 2 )
    img3 = cv2.line(img3, (dst_box[0][3],dst_box[1][3]), (dst_box[0][0],dst_box[1][0]), (255,0,22), thickness = 2 )

plt.imshow(img3)
plt.show()

