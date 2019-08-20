'''
Created on Aug 8, 2019

@author: jsaavedr
'''

import basis
import pai_io
import bw
import skimage.measure as measure
import matplotlib.pyplot as plt
import scipy.ndimage.morphology as morph 
if __name__ == '__main__' :
    filename ='../images/gray/rice.jpg'
    image=pai_io.imread(filename, as_gray = True)
    #image processing
    th_otsu = basis.get_threshold_otsu(image)
    bin_image = basis.threshold(image, th_otsu)
    cc_list = bw.get_ccomponents(bin_image)
    cc_list = bw.remove_small_components(cc_list, 50)    
    bin_image1 = bw.cc2image(cc_list, image.shape)
    bin_image1 = morph.binary_fill_holes(bin_image1)
    labels, ncc = measure.label(bin_image1, return_num = True)
    print('nc : {}'.format(ncc))
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_title('Image')
    xs[1].imshow(bin_image1, cmap = 'gray')
    xs[1].set_title('Binary')
    xs[2].imshow(labels, cmap = 'jet')
    xs[2].set_title('Labels nc:{}'.format(ncc))
    plt.show()