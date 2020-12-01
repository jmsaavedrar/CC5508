import sys
sys.path.append('/home/jsaavedr/Research/git/cursos/CC5508')
import scipy.ndimage.filters as nd_filters
import pai_basic.utils as utils
import pai_basic.pai_io as pai_io
import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.morphology as morph
import skimage.filters as filters
import numpy as np

if __name__ == '__main__' :
    #filename = '../images/gray/rice.jpg'
    filename = '../images/gray/four_coins.png'    
    #filename = '../images/gray/ten_coins.png'
    image = pai_io.imread(filename, as_gray = True)    
    image_g = filters.median(image, morph.disk(2))    
    image_grad = utils.get_magnitude(image_g, np.array([[-1,0,1], [-2,0,2], [-1,0,1]]))#
    image_grad[image_grad<100] = 0         
    watershed = seg.watershed(image_grad, watershed_line=True)
    watershed[watershed>1]=watershed[watershed>1] + 10    
    fig, xs = plt.subplots(1,3)
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_axis_off()
    xs[0].set_title('Imagen')
    xs[1].imshow(image_grad, cmap = 'gray')
    xs[1].set_axis_off()
    xs[1].set_title('Mag. Gradientes')
    xs[2].imshow(watershed, cmap = 'gray')
    xs[2].set_axis_off()
    xs[2].set_title('Watershed')    
    plt.show()
    
    
 