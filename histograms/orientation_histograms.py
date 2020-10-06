import scipy.ndimage.filters as nd_filters
import numpy as np
from numpy import arctan2

def compute_orientation_histogram_basic(image, K):
    h = np.zeros(K, np.float32)
    gx_mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    gy_mask = np.transpose(gx_mask)
    gx = nd_filters.convolve(image.astype(np.float32), gx_mask)
    gy = nd_filters.convolve(image.astype(np.float32), gy_mask)
    ang = np.arctan2(gy,gx)    
    ang[ang < 0] = ang[ang < 0] + np.pi #sin signo    
    indx = np.round(K * ang / np.pi) 
    indx[indx ==  K] = 0
    for i in range(K):            
        h[i] = np.sum(indx == i)    
    return h    


def compute_orientation_histogram(image, K):
    h = np.zeros(K, np.float32)
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


def compute_local_orientations(image, cell_size):
    Gx_local = np.zeros((cell_size, cell_size), dtype = np.float32)
    Gy_local = np.zeros((cell_size, cell_size), dtype = np.float32)
    r_local = np.zeros((cell_size, cell_size), dtype = np.float32)    
    gx_mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    gy_mask = np.transpose(gx_mask)
    gx = nd_filters.convolve(image.astype(np.float32), gx_mask)
    gy = nd_filters.convolve(image.astype(np.float32), gy_mask)
    mag = np.sqrt(np.square(gy) + np.square(gx))
    idx_rows, idx_cols = np.indices(image.shape)
    idx_grid_rows = np.floor(cell_size * idx_rows / image.shape[0])
    idx_grid_cols = np.floor(cell_size * idx_cols / image.shape[1])
    print(idx_grid_rows)
    for p in np.arange(cell_size) :
        for q in np.arange(cell_size) :
            rows, cols = np.where((idx_grid_rows == p) & (idx_grid_cols == q))
            local_gx = gx[rows, cols]
            local_gy = gy[rows, cols]
            local_mag = mag[rows, cols]            
            Gx_local[p,q] = np.sum((np.square(local_gx) - np.square(local_gy))) 
            Gy_local[p,q] = np.sum(2.0*(local_gx*local_gy))
            r_local[p,q] = np.mean(local_mag)
    local_ang = arctan2(Gy_local, Gx_local) * 0.5
    local_ang = local_ang + np.pi*0.5 # 0 <= ang  <= pi    
    return local_ang,  r_local
    