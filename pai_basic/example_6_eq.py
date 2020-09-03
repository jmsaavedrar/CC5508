'''
Created on Aug 6, 2019

@author: jsaavedr

Histogram equalization
'''
import matplotlib.pyplot as plt
import pai_io
import basis

if __name__ == '__main__' :
    filename ='../images/gray/im_3.tif'
    image=pai_io.imread(filename, as_gray = True)
    im_eq = basis.equalize_image(image)    
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title('Original')
    xs[1].imshow(im_eq, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Equalized')    
    plt.show()
