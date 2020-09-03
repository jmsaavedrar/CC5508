'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import skimage.filters as filters
import skimage.morphology as morphology
import scipy.ndimage.filters as nd_filters
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/ruido.tif'
    image=pai_io.imread(filename, as_gray = True)    
    strel=morphology.square(3)
    image_median=filters.median(image, strel)
    g_kernel = basis.get_gaussian2d(2, 6)
    image_g = nd_filters.convolve(image, g_kernel, mode='constant', cval=0)        
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(image_g, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Filtro Gaussiano')
    xs[2].imshow(image_median, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Filtro Mediana')
    plt.show()