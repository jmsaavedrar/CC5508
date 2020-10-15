import sys
sys.path.append('../pai_basic')
import utils
import pai_io
import orientation_histograms as oh
import matplotlib.pyplot as plt
import numpy as np
 
if __name__ == '__main__' :
    #filename = '../images/gray/lion_gray.jpg'
    filename = '../images/sketches/547.png'
    #filename = '/home/jsaavedr/Documents/Docencia/2020/CC5508/tareas/tarea2/circular/fp_circ_9.png'
    #filename = '../images/finger/105_4.tif'
    #filename = '/home/jsaavedr/Documents/Docencia/2020/CC5508/tareas/tarea2/arch/fp_arch.png'
    #filename = '/home/jsaavedr/Documents/Docencia/2020/CC5508/tareas/tarea2/loop/fp_lf_7.png' 
    #filename = '../images/gray/im_31.png'    
    imageA = pai_io.imread(filename, as_gray = True)
    K = 16
    A, R = oh.compute_local_orientations(imageA,K)
    ys = np.arange(K)
    xs = np.arange(K)
    ys = np.floor(( (ys + 0.5) / K ) * imageA.shape[0])
    xs = np.floor(( (xs + 0.5) / K ) * imageA.shape[1])     
    plt.imshow(imageA, cmap = 'gray', vmax = 255, vmin = 0) 
    plt.quiver(xs, ys, np.cos(A)*R, np.sin(A)*R, angles = 'xy', color = 'r')
    plt.axis('off')         
    plt.show()
    
