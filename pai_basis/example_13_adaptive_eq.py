'''
Created on Aug 6, 2019

@author: jsaavedr
Otsu
'''

import matplotlib.pyplot as plt
import basis
import pai_io
import skimage.exposure as exposure
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/mri.tif'
    #filename ='../images/gray/im_3.tif'
    filename ='../images/gray/Lowcontr.tif'
    image=pai_io.imread(filename, as_gray = True)
    image_eq = basis.to_uint8(exposure.equalize_hist(image))
    image_eqa = basis.to_uint8(exposure.equalize_adapthist(image,clip_limit=0.1))
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(image_eq, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Eq')
    xs[2].imshow(image_eqa, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Adaptive Eq')
    plt.show()