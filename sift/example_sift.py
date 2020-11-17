#pip install opencv-python
import cv2
from matplotlib import pyplot as plt

#img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)          # queryImage
img1 = cv2.imread('../images/sift/simple.png',cv2.IMREAD_GRAYSCALE)          # queryImage
# Initiate SIFT detector
print(img1.shape)
sift = cv2.SIFT_create(contrastThreshold = 0.2, sigma = 0.71)
kp = sift.detect(img1,None)
print(len(kp))
for kp_i in kp [:10] :    
    print("{} {}".format(kp_i.size, kp_i.pt))    
img=cv2.drawKeypoints(img1,kp, img1, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img)
plt.show()

