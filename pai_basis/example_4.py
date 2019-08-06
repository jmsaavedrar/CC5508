'''
Created on Aug 1, 2019

@author: jsaavedr
Thresholding
'''

import matplotlib.pyplot as plt
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/car_1.png'
    image=pai_io.imread(filename)
    th = image.max() * 0.5
    print('th = {}'.format(th))
    bin_image = 1 - basis.threshold(image, th)    
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(bin_image*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Thresholded image')
    plt.show()