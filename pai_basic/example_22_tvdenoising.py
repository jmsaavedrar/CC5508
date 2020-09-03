'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import skimage.restoration as restor
import pai_io
import numpy as np

if __name__ == '__main__' :
    filename ='../images/gray/lenna_gray_noisy.png'
    image = pai_io.imread(filename, as_gray = True)
    print(image)
    image_1 = image
    image_1 = restor.denoise_tv_chambolle(image, 0.2)            
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    xs[0].set_title('Image')
    xs[1].imshow((image_1*255).astype(np.uint8), cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title('Denoised Image')
    plt.show()
    
    
    