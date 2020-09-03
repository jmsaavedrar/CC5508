'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd_filters
import pai_io
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/elephant.jpg'
    filename ='../images/gray/chair_gray.jpg'
    #filename ='../images/gray/im_2.tif'
    image=pai_io.imread(filename, as_gray = True)
    gx_kernel = np.array([[0,-1,1]])
    gy_kernel = np.transpose(gx_kernel)
    print(gy_kernel)    
    gx = nd_filters.convolve(image.astype(np.float32), gx_kernel, mode='constant', cval=0)
    print(gx.dtype)
    gx = 1-(np.abs(gx) / np.max(gx))
    gy = nd_filters.convolve(image.astype(np.float32), gy_kernel, mode='constant', cval=0)
    gy = 1- (np.abs(gy) / np.max(gy))       
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(gx, cmap = 'gray')
    xs[1].set_title('gx')
    xs[2].imshow(gy, cmap = 'gray')
    xs[2].set_title('gy')
    plt.show()