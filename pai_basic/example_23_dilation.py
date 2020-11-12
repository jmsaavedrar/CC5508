'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import pai_io
import skimage.morphology as morph
import utils

if __name__ == '__main__' :
    #filename ='../images/gray/lenna_gray_noisy.png'
    filename = '../images/gray/rice.jpg'
    image = pai_io.imread(filename, as_gray = True)   
    image_opening = morph.opening(image, morph.disk(31))    
    image_processed = image - image_opening
    th = utils.get_threshold_otsu(image_processed)
    bin= utils.threshold(image_processed, th)
    bin = morph.binary_opening(bin, morph.disk(11))
    ig, ax = plt.subplots(1,3)
    ax[0].imshow(image, cmap = 'gray')
    ax[0].set_title('image')
    ax[1].imshow(image_processed, cmap = 'gray', vmin=0, vmax = 255)
    ax[1].set_title('image_p')    
    ax[2].imshow(bin*255, cmap = 'gray', vmin=0, vmax = 255)
    ax[2].set_title('bin')
    for i in range(3) :        
            ax[i].set_axis_off()
    plt.show()
#     A = np.array([[0,0,0,0,0],
#                  [0,1,1,1,0],
#                  [0,1,1,1,0],
#                  [0,1,1,1,0],
#                  [0,0,0,0,0]]
#                  )
#     B =np.array([[1,1,0]])
#     C = morph.binary_dilation(A,B)
#     print(C.astype(np.uint8))
#     