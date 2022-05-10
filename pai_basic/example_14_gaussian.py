'''
Created on Aug 6, 2019

@author: jsaavedr
Gaussian
'''

import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd_filters
import numpy as np
import utils
import pai_io

if __name__ == '__main__' :
    
    #filename ='../images/gray/rice.jpg'
    #filename ='../images/gray/ruido.tif'
    filename ='../images/gray/lenna_gray_noisy.png'
    image=pai_io.imread(filename, as_gray = True)
    g_kernel = utils.get_gaussian2d(sigma = 5, radius = 15)
    print(g_kernel)    
    image_g = nd_filters.convolve(image, g_kernel, mode='constant', cval=0)
    print((g_kernel*100).astype(np.int32) / 100.0)
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(g_kernel, cmap = 'gray')
    xs[0].set_title('kernel')
    xs[1].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Imagen')
    xs[2].imshow(image_g, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Imagen Filtrada')
    plt.show()