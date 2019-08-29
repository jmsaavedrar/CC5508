import scipy.ndimage.filters as nd_filters
import numpy as np

def compute_orientation_histogram(image, K):
    h = np.zeros( K, np.float32)
    gx_mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    gy_mask = np.transpose(gx_mask)
    gx = nd_filters.convolve(image.astype(np.float32), gx_mask)
    gy = nd_filters.convolve(image.astype(np.float32), gy_mask)
    ang = np.arctan2(gy,gx)    
    ang[ang < 0] = ang[ang < 0] + np.pi #sin signo
    mag = np.sqrt(np.square(gy) + np.square(gx))    
    indx = np.round(K * ang / np.pi) 
    indx[indx ==  K] = 0
    for i in range(K):
        rows, cols = np.where(indx  == i)        
        h[i] = np.sum(mag[rows, cols])
    h =  h / np.linalg.norm(h,2)  #vector unitario    
    return h
    