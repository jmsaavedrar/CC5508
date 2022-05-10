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
    fig, xs = plt.subplots(1,3)
    for i in range(3):
        xs[i].set_axis_off()
    xs[0].imshow(image_1, cmap = 'gray')
    xs[0].set_title('Original')
    xs[1].imshow(image, cmap = 'gray')
    xs[1].set_title('LSB')
    xs[2].imshow(hidden_image * 255, cmap = 'gray')
    xs[2].set_title('Hidden')
    plt.show()