'''
Created on Aug 1, 2019

@author: jsaavedr

A simple example for reading images with skimage
scikit-image
pip install scikit-image
'''
import skimage.io as io
import matplotlib.pyplot as plt


if __name__ == '__main__':
    filename = '../images/gray/lion_gray.jpg'
    #filename = '../images/color/fichas.jpg'
    image = io.imread(filename, as_gray = 'True')
    print(image[10:15,10:15]) 
    #0..249 x 0..249  
    print('shape: {} dtype: {}'.format(image.shape, image.dtype))
    ##showing image
    plt.imshow (image, cmap = 'gray')
    plt.title('image')
    plt.axis('off')
    plt.show()