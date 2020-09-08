'''
Created on Aug 6, 2019

@author: jsaavedr

Histogram equalization
'''
import matplotlib.pyplot as plt
import pai_io
import utils
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/im_3.tif'
    filename = '../images/gray/Lowcontr.tif'
    image=pai_io.imread(filename, as_gray = True)
    h = utils.get_histogram(image)
    im_eq = utils.equalize_image(image)
    h_eq = utils.get_histogram(im_eq)        
    fig, xs = plt.subplots(2,2)
    for i in range(2):
        xs[0,i].set_axis_off()    
    xs[0,0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0,0].set_title('Original')        
    xs[0,1].imshow(im_eq, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0,1].set_title('Equalized')   
    xs[1,0].bar(x=np.arange(256), height = h) 
    xs[1,1].bar(x=np.arange(256), height = h_eq)
    plt.show()
