import numpy as np
import cv2


def get_perspective(pts_src, pts_dst):
    """
    pts_src: es una lista de puntos(x,y) en la imagen origen
    pts_dst: es una lista de puntos(x,y) en la imagen destino
    
    pts_src->pts_dst representan correspondencias
    
    len(pts_src) == len(pts_dst) == 4
    """
    #assert(len(pts_src) == 4, "not enough points")
    #assert(len(pts_dst) == 4, "not enough points")    
    A = np.zeros((8,8), dtype = np.float32)
    b = np.zeros((8,1), dtype = np.float32)
    R = np.zeros((9,1), dtype = np.float32)
    for i in range(4) :
        i1 = i*2
        i2 = i*2 + 1 
        A[i1][0] = pts_src[i][0]
        A[i1][1] = pts_src[i][1]
        A[i1][2] = 1
        A[i1][6] = - pts_src[i][0]*pts_dst[i][0]
        A[i1][7] = - pts_src[i][1]*pts_dst[i][0]        
        b[i1] = pts_dst[i][0]
        
        A[i2][3] = pts_src[i][0]
        A[i2][4] = pts_src[i][1]
        A[i2][5] = 1
        A[i2][6] = - pts_src[i][0]*pts_dst[i][1]
        A[i2][7] = - pts_src[i][1]*pts_dst[i][1]
        b[i2] = pts_dst[i][1]
        
    #alpha = np.linalg.solve(A,b)
    alpha = np.matmul(np.linalg.pinv(A), b)
    R[:8] = alpha    
    R[8] = 1
    R = np.reshape(R, (3,3))
    return R


def bi_interpol(image, x, y):
    """
    interpolación bilineal
    x: es un punto real en la coordenada x en imagen
    y: es un punto real en la coordenada y en imagen
    """
    x_left = int(np.floor(x))
    x_right = x_left + 1
    y_top = int(np.floor(y)) 
    y_bottom = y_top + 1
    
    w_left = 1 - (x - x_left)
    w_right = 1 - w_left
    w_top = 1 - (y - y_top)
    w_bottom = 1 - w_top
    #aquí se interpola
    val =  image[y_top][x_left]*w_top*w_left 
    val += image[y_top][x_right]*w_top*w_right 
    val += image[y_bottom][x_left]*w_bottom*w_left 
    val += image[y_bottom][x_right]*w_bottom*w_right
    return val

def warp_image(image, R):
    """
    la imagen image se transforma usando R
    R será la transformación inversa, que va desde el destino al origen
    image es el origen
    """
    image_out = np.zeros(image.shape, dtype = image.dtype)
    xs, ys = np.meshgrid(np.arange(image_out.shape[1]), np.arange(image_out.shape[0]))
    xs = np.reshape(xs, (1,-1))
    ys = np.reshape(ys, (1,-1))
    zs = np.ones(ys.shape, dtype = np.float32)
    points = np.concatenate((xs,ys,zs), axis = 0)
    #points representa puntos en el destino, o sea en image_out
    #transformacion en perspectiva (homografia)
    new_points = np.matmul(R,points)
    new_points = new_points / new_points[2,:]
    #new_points son puntos en imagen
    #----------------------------------------    
    n = new_points.shape[1]
    for i in np.arange(n) :
        x = new_points[0][i]
        y = new_points[1][i]        
        if  x > 0 and (x < image.shape[1] - 1) and y > 0 and (y < image.shape[0]  - 1):          
            image_out[int(points[1][i])][int(points[0][i])] = bi_interpol(image, x, y)
    return image_out

def estimate_transformation(src, dst, th_dist = 5):
    """
    implementa un método para estimar una buena transformación entre matches de SIFT
    RANSAC
    """
    n_repeat = 50
    #matches = sorted(matches, key = lambda x:  x.distance)
    n_matches = src.shape[1]
    #matches = matches[:n_matches]
    print(n_matches)
    #ransac random sample consensus
    max_inliers = 0
    for _ in range(n_repeat) :
        random_pos = np.random.randint(n_matches, size = 4) 
        pts1 = []
        pts2 = []
        for j in range(4) :
            pts1.append((src[0][random_pos[j]], src[1][random_pos[j]]))
            pts2.append((dst[0][random_pos[j]], dst[1][random_pos[j]]))
        T = get_perspective(pts1, pts2)
        #aplico la homografía
        points_t = np.matmul(T,src)
        points_t = points_t/points_t[2,:]
        #compute number of inliers
        d_error = np.sqrt(np.sum(np.square(dst[0:2,:] - points_t[0:2,:]), axis = 0))
        n_inliers = np.sum(d_error <= th_dist)
        if n_inliers > max_inliers :
            best_T = T
            max_inliers = n_inliers
    print(max_inliers)           
    return best_T

if __name__ == '__main__':
    print('a')
    #fontana
    filename = '../images/stitching/fontana_3.jpg'
    #filename = '../images/stitching/perspectiva.jpg'
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) 
    pts1 = [(337,207), (567,270), (337,568), (580,568)]
    pts2 = [(337,207), (580,207), (337,568), (580,568)]
    #pts1 = [(233,245), (349,234), (349,416), (233,416)]
    #pts2 = [(233,245), (349,245), (349,416), (233,416)]
    #por qué al revés?    
    T =get_perspective(pts2, pts1)
    image_out = warp_image(image, T)
    cv2.imshow("image_in", image)
    cv2.imshow("image_out", image_out)
    cv2.waitKey()    
    