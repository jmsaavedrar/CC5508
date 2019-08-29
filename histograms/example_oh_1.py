import sys
sys.path.append('../pai_basis')
import basis
import pai_io
import orientation_histograms as oh
import matplotlib.pyplot as plt
import numpy as np
 
if __name__ == '__main__' :
    #filename = '../images/gray/im_34.png'
    #filename = '../images/gray/im_2.tif'
    filenameA = '../images/gray/elephant.jpg'
    filenameB = '/home/jsaavedr/Documents/Datasets/SBIR/dataset_1/BD_2/chair/180016.jpg'
    imageA = pai_io.imread(filenameA, as_gray = True)
    imageB = pai_io.imread(filenameB, as_gray = True)
    K = 36
    hA = oh.compute_orientation_histogram(imageA,K)
    hB = oh.compute_orientation_histogram(imageB,K)
    distancia = np.sqrt(np.sum(np.square(hA - hB)))
    print('distancia = {}'.format(distancia))
    fig, xs = plt.subplots(2,2)
    xs[0,0].imshow(imageA, cmap='gray')
    xs[0,1].bar(range(K), height = hA)
    xs[1,0].imshow(imageB, cmap='gray')
    xs[1,1].bar(range(K), height = hB)
    plt.show()    
