'''
Created on Aug 6, 2019

@author: jsaavedr
Adding Gaussian Noise
'''

import matplotlib.pyplot as plt
import scipy.ndimage.filters as nd_filters
import skimage.filters as filters
import skimage.io as io
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/lenna_gray.png'
    image=pai_io.imread(filename, as_gray = True)    
    noisy_image = basis.add_gaussian_noise(image, 20)
    #io.imsave(filename+"noisy.png", noisy_image)
    g_kernel = basis.get_gaussian2d(1, 3)
    image_g = nd_filters.convolve(image, g_kernel, mode='constant', cval=0)     
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(noisy_image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Ruido Gaussiano')
    xs[2].imshow(image_g, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Imagen Filtrada')
    plt.show()