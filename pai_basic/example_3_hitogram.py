'''
Created on Aug 1, 2019

@author: jsaavedr
Image Histogram
'''


import numpy as np
import matplotlib.pyplot as plt
import pai_io
import utils

if __name__ == '__main__' :
    #filename ='../images/gray/ten_coins.png'    
    #image=pai_io.imread(filename)
    image = np.zeros((400,400), dtype = np.uint8)
    image[100:170, 200:270] = 255    
    h = utils.get_histogram(image)
    fig, xs = plt.subplots(1,2)
    xs[0].set_axis_off()    
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[1].bar(x=np.arange(256), height = h)
    plt.show()
    








