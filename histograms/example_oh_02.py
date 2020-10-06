import sys
sys.path.append('../pai_basic')
import utils
import pai_io
import orientation_histograms as oh
import matplotlib.pyplot as plt
import numpy as np
 
if __name__ == '__main__' :    
    filenameA = '../images/digits/digit_mnist_00100_9.png'
    filenameB = '../images/digits/digit_mnist_00059_9.png'    
    #filenameB = '../images/digits/digit_mnist_00376_5.png'
    #filenameA = '../images/digits/digit_mnist_00011_0.png'
    #filenameB = '../images/digits/digit_mnist_00381_0.png'
    #filenameB = '../images/digits/digit_mnist_00376_5.png'
    #filenameB = '../images/digits/digit_mnist_00478_2.png'    
    imageA = pai_io.imread(filenameA, as_gray = True)
    imageB = pai_io.imread(filenameB, as_gray = True)
    K = 36
    hA = oh.compute_orientation_histogram(imageA,K)
    hB = oh.compute_orientation_histogram(imageB,K)
    distancia= np.sqrt(np.sum(np.square(hA - hB)))
    print('distancia = {}'.format(distancia))
    fig, xs = plt.subplots(2,2)
    xs[0,0].imshow(imageA, cmap='gray')
    xs[0,1].bar(range(K), height = hA)
    xs[1,0].imshow(imageB, cmap='gray')
    xs[1,1].bar(range(K), height = hB)
    plt.show()    
