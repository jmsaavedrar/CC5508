'''
Created on Aug 1, 2019

@author: jsaavedr
Reading an image
'''
import pai_io
import matplotlib.pyplot as plt


if __name__ == '__main__':
    filename = '../images/gray/lion_gray.jpg' 
    image = pai_io.imread(filename, as_gray = True)
    print('shape: {}'.format(image.shape))
    ##showing image
    plt.imshow (image, cmap = 'gray')
    plt.title('image')
    plt.axis('off')
    plt.show()