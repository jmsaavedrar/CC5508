'''
Created on Aug 1, 2019

@author: jsaavedr

A simple example for reading images with skimage
'''
import skimage.io as io
import matplotlib.pyplot as plt



if __name__ == '__main__':
    filename = '../images/gray/lion_gray.jpg'
    filename = '../images/color/fichas.jpg'
    image = io.imread(filename)    
    print('shape: {} dtype: {}'.format(image.shape, image.dtype))
    ##showing image
    plt.imshow (image, cmap = 'gray')
    plt.title('image')
    plt.axis('off')
    plt.show()