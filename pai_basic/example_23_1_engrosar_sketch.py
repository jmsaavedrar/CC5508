import matplotlib.pyplot as plt
import pai_io
import skimage.morphology as morph
import utils

if __name__ == '__main__' :
    #filename ='../images/gray/lenna_gray_noisy.png'
    filename = '/home/jsaavedr/Pictures/sketch.png'
    image = pai_io.imread(filename, as_gray = True)   
    th = 150
    bin= 1 - utils.threshold(image, th)
    bin = 1  -morph.binary_dilation(bin, morph.disk(3))
    fig, ax = plt.subplots(1,3)
    ax[0].imshow(image, cmap = 'gray')
    ax[0].set_title('image')
    ax[1].imshow(bin * 255, cmap = 'gray', vmin=0, vmax = 255)
    ax[1].set_title('image_p')    
   
    for i in range(3) :        
            ax[i].set_axis_off()
    plt.show()

    