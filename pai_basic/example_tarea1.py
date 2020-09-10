import matplotlib.pyplot as plt
import utils
import pai_io
import numpy as np

if __name__ == '__main__' :
    #filename ='../images/gray/rice.jpg'
    filename ='../images/gray/ten_coins.png'
    image=pai_io.imread(filename)
    image_1 = image.copy()
            
    bin_image = utils.threshold(image, 100)    
    image = utils.set_image_on_lsb(image, bin_image)
    hidden_image = utils.get_image_from_lsb(image)    
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].set_axis_off()
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_title('Imagen A')
    xs[1].imshow(image_1, cmap = 'gray')
    xs[1].set_title('Image B')
    plt.show()