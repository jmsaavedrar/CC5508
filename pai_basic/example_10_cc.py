'''
Created on Aug 8, 2019

@author: jsaavedr
'''

import basis
import pai_io
import bw
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
    cc_list = bw.get_ccomponents(bin_image1)
    bin_boundary = bw.cc2image(cc_list, image.shape, 'boundary')
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_title('Image')
    xs[1].imshow(1-bin_boundary, cmap = 'gray')
    xs[1].set_title('Boundary nc:{}'.format(len(cc_list)))
    '''for cc in cc_list :
        bbox = cc['bbox']
        rect = patches.Rectangle((bbox[1], bbox[0]), bbox[3],bbox[2], edgecolor = 'r', linewidth = '2', facecolor = 'none')
        xs[1].add_patch(rect)
    '''
    plt.show()