'''
Created on Aug 1, 2019

@author: jsaavedr
Thresholding
'''

import matplotlib.pyplot as plt
import utils
import pai_io

if __name__ == '__main__' :
    #filename ='../images/gray/rice.jpg'
    filename ='../images/gray/ten_coins.png'
    image=pai_io.imread(filename)
    th =100
    #th = image.max() * 0.5
    print('th = {}'.format(th))
    bin_image = utils.threshold(image, th)    
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_title('Original')
    xs[1].imshow(bin_image*255, cmap = 'gray')
    xs[1].set_title('Thresholded image')
    plt.show()