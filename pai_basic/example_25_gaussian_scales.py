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
    
    filename ='../images/gray/lenna_gray.png'
    image=pai_io.imread(filename, as_gray = True)
    g_kernel = utils.get_gaussian2d(sigma = 2, radius = 6)    
    images_g =[image]
    lps = []
    for i  in range(1,4) :
        images_g.append(nd_filters.convolve(images_g[i-1], g_kernel, mode='constant', cval=0))
        lps.append(images_g[i] - images_g[i-1])   
         
    
    #dog = image_g2 - image_g1 
    
    fig, xs = plt.subplots(2,4)
    for i in range(4):
        xs[0,i].set_axis_off()
        xs[1,i].set_axis_off()
    xs[0,0].imshow(image, cmap = 'gray')
    xs[0,0].set_title('Image')
    for i in range(4) :
        xs[0,i].imshow(images_g[i], cmap = 'gray', vmin = 0, vmax = 255)
        xs[0,i].set_title('Gaussian_{}'.format(i))
    for i in range(0,3) :
        xs[1,i+1].imshow(lps[i], cmap = 'gray', vmin = 0, vmax = 255)
        xs[1,i+1].set_title('Laplacian_{}'.format(i+1))
    
    plt.show()