#pip install opencv-python
import cv2
from matplotlib import pyplot as plt

#just o unpack_octave information
def unpack_octave(octave):
    """Compute octave, layer, and scale from a keypoint
    """
    octave = octave & 255
    layer = (octave >> 8) & 255
    if octave >= 128:
        octave = octave | -128
    scale = 1 / float(1 << octave) if octave >= 0 else float(1 << -octave)
    return octave, layer, scale


#img1 = cv2.imread('../images/sift/box.png',cv2.IMREAD_GRAYSCALE)          # queryImage
img1 = cv2.imread('../images/sift/simple.png',cv2.IMREAD_GRAYSCALE)          # queryImage
# Initiate SIFT detector
print(img1.shape)
sift = cv2.SIFT_create()
#sift = cv2.SIFT_create(contrastThreshold = 0.2, sigma = 0.71)
kp = sift.detect(img1,None)
print(len(kp))
for kp_i in kp[:10] :    
    #octave = kp_i.octave & 255
    octave, layer, scale_factor = unpack_octave(kp_i.octave)
    print("{} {}  {} {}".format(kp_i.size, kp_i.pt, octave, layer))    
img=cv2.drawKeypoints(img1,kp, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img)
plt.show()

