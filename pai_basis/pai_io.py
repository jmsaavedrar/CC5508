'''
Created on Aug 1, 2019

@author: jsaavedr
io functions
'''
import skimage.io as skio
import numpy as np
import basis

def imread(filename, as_gray = False):
    image = skio.imread(filename, as_gray = as_gray)
    if image.dtype == np.float64 :
        image = basis.to_uint8(image)
    return image
