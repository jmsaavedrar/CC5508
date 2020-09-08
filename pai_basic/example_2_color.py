'''
Created on Aug 1, 2019

@author: jsaavedr
Reading a color image
'''
import pai_io
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = '../images/color/rgb_cube.png' 
    #filename = '../images/color/fichas.jpg'
    image = pai_io.imread(filename)
    print('shape: {}'.format(image.shape))
    im_red = image[:,:,0];
    im_green = image[:,:,1];
    im_blue = image[:,:,2];    
    ##showing image
    n_rows = 2
    n_cols = 3
    fig, ax = plt.subplots(n_rows, n_cols)
    ax[0,1].imshow(image)
    ax[0,1].set_title('image')
    ax[1,0].imshow(im_red, cmap = 'gray')
    ax[1,0].set_title('Red')
    ax[1,1].imshow(im_green, cmap = 'gray')
    ax[1,1].set_title('Green')
    ax[1,2].imshow(im_blue, cmap = 'gray')
    ax[1,2].set_title('Blue')
    for i in range(n_rows) :
        for j in range(n_cols) :
            ax[i,j].set_axis_off()
    plt.show()