'''
Created on Aug 6, 2019

@author: jsaavedr
Filtro Mediana
'''

import matplotlib.pyplot as plt
import pai_io
import skimage.morphology as morph
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/lenna_gray_noisy.png'
    #image = pai_io.imread(filename, as_gray = True)
    A = np.array([[0,0,0,0,0],
                [0,1,1,1,0],
                [0,1,1,1,0],
                [0,1,1,1,0],
                [0,0,0,0,0]]
                )
    B =np.array([[1,1,0]])
    C = morph.binary_dilation(A,B)
    print(C.astype(np.uint8))