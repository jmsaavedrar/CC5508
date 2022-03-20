'''
Created on Aug 1, 2019

@author: jsaavedr

As skimage.io.imread may return images with diferent dtype (float64 or unit8), in this example we'll use a cutomized imread, that always
returns a uint8 image.
'''
import pai_io
import matplotlib.pyplot as plt


if __name__ == '__main__':
    #filename = '../images/gray/lion_gray.jpg'
    #filename = '../images/color/rgb.png'
    filename = '../images/color/fichas.jpg'
    image = pai_io.imread(filename, as_gray = True)
    print(image) 
    print('shape: {} dtype: {}'.format(image.shape, image.dtype))
    ##showing image
    plt.imshow (image, cmap = 'gray')
    plt.title('image')
    plt.axis('off')
    plt.show()