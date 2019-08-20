'''
Created on Aug 7, 2019

@author: jsaavedr
'''
import basis
import pai_io
import bw
import skimage.measure as measure
import matplotlib.pyplot as plt 
if __name__ == '__main__' :
    filename ='../images/gray/ten_coins.png'
    image=pai_io.imread(filename, as_gray = True)
    th_otsu = basis.get_threshold_otsu(image)
    bin_image = basis.threshold(image, th_otsu)
    print(bin_image.shape)
    label, num = measure.label(bin_image, return_num = True)
    
    fig, xs = plt.subplots(1,3)
    xs[0].imshow(image, cmap = 'gray')
    xs[0].set_title('Image')
    xs[1].imshow(bin_image, cmap = 'gray')
    xs[1].set_title('Binary')
    xs[2].imshow(label, cmap='jet')
    xs[2].set_title('Labels nc : {}'.format(num))
    for i in range(3):
        xs[i].set_axis_off()
    plt.show()    
    #cc = bw.getCC(bin_image)    
    #print(len(cc))