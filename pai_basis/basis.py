'''
pai_basic.basis module
A set of basic functions to operate on gray-scale images
@author: jsaavedr
'''
import numpy as np
import scipy.ndimage.filters as nd_filters

#get histogram of an image
def get_histogram(gray_im):
    h=np.zeros(256, dtype=np.float32)
    for i in range(gray_im.shape[0]):
        for j in range(gray_im.shape[1]):
            h[gray_im[i,j]]+=1.0
    return h
#----------------------------------------------
def threshold(gray_im, th):
    bin_im = np.zeros(gray_im.shape, np.uint8)
    bin_im[gray_im>=th]=1
    return bin_im
#----------------------------------------------
#compute accum
def get_accum(histogram, length=256):
    accum=np.zeros(length)
    accum[0]=histogram[0]
    for i in range(1,length):
        accum[i]=accum[i-1]+histogram[i]
    return accum
    
#det otsu
def get_threshold_otsu(gray_im):    
    h = get_histogram(gray_im)
    h = h / np.sum(h)    
    accum = get_accum(h)
    media_t = np.zeros(256,  np.float32)
    #compute media for each t in [0..255]
    for i in range(0,256):
        media_t[i] = media_t[i-1] + i*h[i] 
    mu = media_t[255]
    best_t = 0
    best_val = 0
    eps = 0.0001
    for t in range(1,256):
        w0 = accum[t]
        w1 = 1.0 - w0        
        mu_0 = media_t[t] / (w0 + eps)
        mu_1 = (mu - media_t[t]) / (w1 + eps)
        val = w0*(mu_0 - mu)*(mu_0 - mu) + w1*(mu_1 - mu)*(mu_1 - mu)
        if val > best_val:
            best_val = val
            best_t = t
    return best_t

#equalization
def equalize_image(gray_im):
    h=get_histogram(gray_im)
    h = h / np.float(gray_im.shape[0]*gray_im.shape[1])
    accum=get_accum(h)
    imeq=np.zeros(gray_im.shape, np.float32)
    for i in range(imeq.shape[0]):
        for j in range(imeq.shape[1]):            
            imeq[i,j]=255.0*accum[gray_im[i,j]]
    return to_uint8(imeq)

#gaussian  2D
def get_gaussian2d(sigma, radius):
    #radius= 3xsigma
    s=np.int(2*radius+1)
    mask=np.zeros([s,s])
    variance=sigma*sigma
    k=1.0/(2.0*np.pi*variance)    
    for u in range(-radius,radius+1,1):
        for v in range(-radius,radius+1,1):
            mask[u+radius, v+radius]=k*np.exp(-(u*u+v*v)/(2*variance))
    return mask    

#escalamiento lineal
def constrast_stretching(gray_im):
    a=gray_im.min()
    b=gray_im.max()
    im_t=np.zeros(gray_im.shape)
    for i in range(gray_im.shape[0]):
        for j in range(gray_im.shape[1]):
            im_t[i,j]=255*(gray_im[i,j]-a)/(b-a)
    return to_uint8(im_t)              

#to uint8
def to_uint8(image) :
    if image.dtype == np.float64 :
        image = image * 255
    image[image<0]=0
    image[image>255]=255
    image = image.astype(np.uint8, copy=False)
    return image

def add_gaussian_noise(image, std):
    noise = np.random.normal(loc = 0, scale = std, size = image.shape) 
    noisy_image = image + noise
    noisy_image[image < 0] = 0
    noisy_image[image > 255] = 255
    return noisy_image.astype(np.uint8);

def get_borde(image, gx_kernel):    
    gy_kernel = np.transpose(gx_kernel)
    gx = nd_filters.convolve(image.astype(np.float32), gx_kernel, mode='constant', cval=0)    
    gy = nd_filters.convolve(image.astype(np.float32), gy_kernel, mode='constant', cval=0)
    borde = np.sqrt(gx**2 + gy**2)
    return borde