'''
Created on Aug 6, 2019

@author: jsaavedr
Otsu
'''

import matplotlib.pyplot as plt
import basis
import pai_io

if __name__ == '__main__' :
    filename ='../images/gray/ten_coins.png'
    image=pai_io.imread(filename, as_gray = True)
    th = image.max() * 0.5
    th_otsu = basis.get_threshold_otsu(image)    
    print('th = {}'.format(th))
    print('th_otsu = {}'.format(th_otsu))
    bin_image = basis.threshold(image, th)
    bin_image_otsu = basis.threshold(image, th_otsu)    
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(bin_image*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Thresholded image')
    xs[2].imshow(bin_image_otsu*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[2].set_title('Otsu')
    plt.show()