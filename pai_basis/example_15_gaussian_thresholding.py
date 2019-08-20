'''
Created on Aug 6, 2019

@author: jsaavedr
Gaussian + Adaptive Thresholding
'''

import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd_filters
import skimage.filters as filters
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/rice.jpg'
    image=pai_io.imread(filename, as_gray = True)
    g_kernel = basis.get_gaussian2d(2, 6)
    image_g = nd_filters.convolve(image, g_kernel, mode='constant', cval=0)
    th_adaptive = filters.threshold_local(image_g, block_size = 255, offset = -5)
    image_bin = (image_g > th_adaptive)     
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(image_g, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Imagen Filtrada')
    xs[2].imshow(image_bin*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Imagen Binaria')
    plt.show()