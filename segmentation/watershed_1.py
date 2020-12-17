import sys
sys.path.append('/home/jsaavedr/Research/git/cursos/CC5508')
import pai_basic.pai_io as pai_io
import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.morphology as morph
import skimage.filters as filters

if __name__ == '__main__' :
    filename = '../images/gray/rice.jpg'
    #filename = '../images/gray/four_coins.png'    
    image = pai_io.imread(filename, as_gray = True)
    image = 255 - image
    image_g = filters.median(image, morph.disk(2))        
    #image_g = morph.closing(image_g, morph.disk(13))
    watershed = seg.watershed(image_g, watershed_line=True)
    image_g[watershed == 0] = 0    
    plt.imshow(image_g, cmap = 'gray')
    plt.axis('off')    
    plt.show()