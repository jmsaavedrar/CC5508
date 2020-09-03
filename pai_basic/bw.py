'''
Created on Aug 7, 2019

@author: jsaavedr
'''
import numpy as np
import skimage.measure as measure

def is_valid(shape, i,j):
    if (i>=0)  and (j>=0) and (i<shape[0]) and (j<shape[1]):
        return True
    else:
        return False
    
        
#getCC
def get_ccomponents(bw_image):
    print("--labeling ")
    bw_sets, n_cc = measure.label(bw_image, return_num = True)
    print("--labeling OK")
    cc_list = []
    for i_cc in range(1, n_cc+1):
        inds=np.where(bw_sets == i_cc)        
        points = list(zip(inds[0].tolist(), inds[1].tolist()))
        min_y = inds[0].min()
        max_y = inds[0].max()
        min_x = inds[1].min()        
        max_x = inds[1].max()
        bbox = (min_y, min_x, max_y - min_y + 1, max_x - min_x + 1)
        boundary = get_boundary(points)
        cc_list.append({'id': i_cc, 
                        'points' : points, 
                        'size': len(points),
                        'bbox': bbox, 
                        'boundary': boundary})
    return cc_list

# remove components with size < target_size
def remove_small_components(cc_list, target_size):
    to_keep = []
    for i, cc in enumerate(cc_list):        
        if (cc['size'] >= target_size):
            to_keep.append(i)    
    new_cc_list = [cc_list[index] for index in to_keep]
    return new_cc_list
    
def cc2image(cc_list, image_shape, type='points'):
    '''
    cc_list : the list of connected components
    image_shape: the target shape
    type : 'points' or 'boundary'
    '''
    image = np.zeros(image_shape)
    for cc in cc_list:
        rows, cols = zip(*cc[type])
        image[rows, cols] = 1
    return image    
            
# digital topology: getBoundary
def get_boundary(cc_points):
    #print (cc_points)
    if len(cc_points) == 1:
        return cc_points
    rows = [p[0] for p in cc_points]
    cols = [p[1] for p in cc_points]
    
    min_x = np.min(cols)
    min_y = np.min(rows)
    max_x = np.max(cols)
    max_y = np.max(rows)
    
    height = max_y - min_y + 1 + 2
    width = max_x - min_x + 1 + 2        
    
    # creating a simple representation of the component
    cc_array = np.zeros([height, width], np.float32)
    # cc_rows and cc_cols with respect to the cc's size
    cc_rows = rows - min_y + 1
    cc_cols = cols - min_x + 1 
    cc_array[ cc_rows, cc_cols ] = 1
    #print(cc_array)
    #neighbors
    l_r=[ 0, -1, -1, -1, 0, 1, 1,  1]
    l_c=[-1, -1,  0,  1, 1, 1, 0, -1]    
    i = cc_rows[0]    
    j = cc_cols[0]
    end = False    
    p1_set = False
    P = (i,j)    
    contour = [P]
    # first point is P
    # point at  right is Q
    idx_q = 0
    P0 = P 
    P1 = (-1,-1)
    #Q0 = (i + l_r[0], j + l_c[0])    
    while not end:        
        Pant = P
        i = P[0]
        j = P[1]        
        idx = idx_q
        #print("{} {} {} ".format(i,j,idx))
        #-------------------------------------------------------
        # moving  Q  P until Q=0 and P=1        
        P = (i + l_r[idx], j + l_c[idx])
        Q = (i + l_r[ (idx -1 + 8) % 8], j + l_c[(idx -1 + 8) % 8])
        while cc_array[P] != 1  or cc_array[Q] != 0 :
            idx = (idx + 1 ) % 8
            Q = P
            P = (i + l_r[ idx ], j + l_c[ idx ])
        #-------------------------------------------------------
        #redefining the position of Q with respect to P        
        if P[0] - Q[0] > 0 : 
            idx_q = 2
        elif P[0] - Q[0] < 0 :
            idx_q = 6
        elif P[1] - Q[1] > 0: 
            idx_q = 0
        elif P[1] - Q[1] < 0: 
            idx_q = 4
        else:
            raise  ValueError("something wrong")                
        # stop condition
        if P == P1 and Pant == P0:
            end = True
        else:
            contour.append(P)            
        if not p1_set :
            P1 = P
            p1_set = True     
    
    # getting back to the real coordinates
    rows_p = [p[0] for p in contour ] 
    cols_p = [p[1] for p in contour ]    
    rows_p = rows_p + min_y - 1
    cols_p = cols_p + min_x - 1
    contour = list(zip(rows_p, cols_p))
    return contour            