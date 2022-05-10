'''
Created on Aug 1, 2019

@author: jsaavedr
Reading a color image combining channels to highlight yellow objects.
'''

import pai_io
import numpy as np
import utils
import matplotlib.pyplot as plt
import utils

if __name__ == '__main__':
    #filename = '../images/color/rgb_cube.png' 
    filename = '../images/color/fichas.jpg'
    #filename = '/home/jsaavedr/Documents/Docencia/2020/CC5508/tareas/tarea3_2020/tarea3/im3.jpg'
    image = pai_io.imread(filename)
    print('shape: {}'.format(image.shape))
    im_red = image[:,:,0];
    im_green = image[:,:,1];
    im_blue = image[:,:,2];
    #yellow
    im_yellow = im_red.astype(np.float64) + im_green.astype(np.float64) - im_blue.astype(np.float64)
    im_yellow = utils.to_uint8(im_yellow / (255.0 + 255.0))    
    ##showing image
    fig, ax = plt.subplots(2,3)
    ax[0,1].imshow(image)
    ax[0,1].set_title('image')
    ax[1,0].imshow(im_red, cmap = 'gray')
    ax[1,0].set_title('Red')
    ax[1,1].imshow(im_green, cmap = 'gray')
    ax[1,1].set_title('Green')
    ax[1,2].imshow(im_yellow, cmap = 'gray')
    ax[1,2].set_title('Yellow')
    for i in range(2) :
        for j in range(3) :
            ax[i,j].set_axis_off()
    plt.show()