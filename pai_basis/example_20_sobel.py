'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd_filters
import basis
import pai_io
import numpy as np

if __name__ == '__main__' :
    filename ='../images/gray/elephant.jpg'
    #filename ='../images/gray/chair_gray.jpg'
    image=pai_io.imread(filename, as_gray = True)
    #g_kernel = basis.get_gaussian2d(2, 6);
    #g_image = nd_filters.convolve(image.astype(np.float32), g_kernel, mode='constant', cval=0)
    image=pai_io.imread(filename, as_gray = True)    
    gx_kernel = np.array([[0,-1,1]])    
    borde = basis.get_borde(image, gx_kernel)
    borde = 1 - borde/np.max(borde)
    
    g_kernel = basis.get_gaussian2d(2, 6)
    image_g = nd_filters.convolve(image, g_kernel)
    
    gx_sobel = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])    
    borde_sobel = basis.get_borde(image_g, gx_sobel)
    borde_sobel = 1 - borde_sobel/np.max(borde_sobel)        
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(borde, cmap = 'gray')
    xs[1].set_title('Basico')
    xs[2].imshow(borde_sobel, cmap = 'gray')
    xs[2].set_title('Sobel')
    plt.show()
    
    