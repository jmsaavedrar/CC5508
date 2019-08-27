'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import skimage.feature as feature
import basis
import pai_io
import numpy as np

if __name__ == '__main__' :
    filename ='../images/gray/elephant.jpg'
    #filename ='../images/gray/chair_gray.jpg'
    image=pai_io.imread(filename, as_gray = True)
    borde_1 = 1 - feature.canny(image, sigma=3)
    borde_2 = 1 - feature.canny(image, sigma=9)        
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow(borde_1, cmap = 'gray')
    xs[1].set_title('Basico')
    xs[2].imshow(borde_2, cmap = 'gray')
    xs[2].set_title('Sobel')
    plt.show()
    
    