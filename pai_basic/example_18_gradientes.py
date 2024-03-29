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
    gx_kernel = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
    #gx_kernel = np.array([[0,-1,1]])
    gy_kernel = np.transpose(gx_kernel)        
    gx = nd_filters.convolve(image.astype(np.float32), gx_kernel, mode='reflect')        
    gy = nd_filters.convolve(image.astype(np.float32), gy_kernel, mode='reflect')
    #visualizamos magnitudes    
    gx = np.abs(gx) / np.sum(np.abs(gx))
    gy = np.abs(gy) / np.sum(np.abs(gy))        
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