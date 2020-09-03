'''
Created on Aug 6, 2019

@author: jsaavedr
Adaptive Threhsolding
'''

import matplotlib.pyplot as plt
import skimage.filters as filters
import numpy as np
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/rice.jpg'
    image=pai_io.imread(filename, as_gray = True)
    print(image.shape)    
    #th_otsu = basis.get_threshold_otsu(image)
    th_adaptive = filters.threshold_local(image, block_size = 201, offset = 1)
    th_niblack = filters.threshold_niblack(image, window_size = 201, k=0.2)
    th_sauvola = filters.threshold_sauvola(image, window_size = 201, k=0.2, r = None)
    #bin_image_otsu = basis.threshold(image, th_otsu)
    bin_image_adaptive = np.uint8(image > th_adaptive)
    bin_image_niblack = np.uint8(image > th_niblack)
    bin_image_sauvola = np.uint8(image > th_sauvola)
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(bin_image_adaptive*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Local')
    xs[1].imshow(bin_image_niblack*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Niblack')
    xs[2].imshow(bin_image_sauvola*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Sauvola')    
    plt.show()