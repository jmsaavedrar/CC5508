import sys
sys.path.append('../pai_basic')
import utils
import pai_io
import orientation_histograms as oh
import matplotlib.pyplot as plt
 
if __name__ == '__main__' :
    filename = '../images/gray/im_30.png'    
    imageA = pai_io.imread(filename, as_gray = True)    
    K = 36
    hA = oh.compute_orientation_histogram(imageA,K)
    fig, xs = plt.subplots(1,2)
    xs[0].imshow(imageA, cmap='gray')
    xs[0].set_title('Input')
    xs[1].bar(range(K), height = hA)
    xs[1].set_title('Histograma de Orientaciones')    
    plt.show()    
