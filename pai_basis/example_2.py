'''
Created on Aug 1, 2019

@author: jsaavedr
Reading a color image
'''

import pai_io
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = '../images/color/fichas.jpg' 
    image = pai_io.imread(filename)
    print('shape: {}'.format(image.shape))
    im_red = image[:,:,0];
    im_green = image[:,:,1];
    im_blue = image[:,:,2];
    ##showing image
    fig, ax = plt.subplots(2,3)
    ax[0,1].imshow(image)
    ax[0,1].set_title('image')
    ax[1,0].imshow(im_red, cmap = 'gray')
    ax[1,0].set_title('R')
    ax[1,1].imshow(im_green, cmap = 'gray')
    ax[1,1].set_title('G')
    ax[1,2].imshow(im_blue, cmap = 'gray')
    ax[1,2].set_title('B')
    for i in range(2) :
        for j in range(3) :
            ax[i,j].set_axis_off()
    plt.show()