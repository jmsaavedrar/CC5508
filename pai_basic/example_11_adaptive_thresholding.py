'''
Created on Aug 6, 2019

@author: jsaavedr
Adaptive Threhsolding
'''

import matplotlib.pyplot as plt
import skimage.filters as filters
import skimage.data as images
import numpy as np
import utils
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/text_4.png'    
    image=pai_io.imread(filename, as_gray = True)
    #image = images.text()
    print(image.shape)    
    th_otsu = utils.get_threshold_otsu(image)
    bin_image_otsu = utils.threshold(image, th_otsu)
    th_adaptive = filters.threshold_local(image, block_size = 15, offset = 21)
    bin_image_adaptive = np.uint8(image > th_adaptive)            
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(bin_image_otsu*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Otsu')
    xs[2].imshow(bin_image_adaptive*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Adaptive')    
    plt.show()