import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)          # queryImage
# Initiate SIFT detector
sift = cv2.SIFT_create()
kp = sift.detect(img1,None)
img = np
img=cv2.drawKeypoints(img1,kp, img1, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img)
plt.show()

