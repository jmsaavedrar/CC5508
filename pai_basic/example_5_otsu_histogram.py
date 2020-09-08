'''
Created on Aug 6, 2019

@author: jsaavedr
Otsu
'''

import matplotlib.pyplot as plt
import utils
import pai_io
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/ten_coins.png'
    #filename = '../images/gray/rice.jpg'
    filename = '../images/gray/four_coins.png'
    #filename = '../images/gray/car_1.png'
    image=pai_io.imread(filename, as_gray = True)    
    th_otsu = utils.get_threshold_otsu(image)        
    print('th_otsu = {}'.format(th_otsu))    
    bin_image_otsu = utils.threshold(image, th_otsu)
    h = utils.get_histogram(image)    
    fig, xs = plt.subplots(1,3)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(bin_image_otsu*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Otsu ={}'.format(th_otsu))
    xs[2].bar(x=np.arange(256), height = h/np.sum(h))
    xs[2].set_title('Histograma'.format(th_otsu))
    plt.show()