#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:18:24 2017

@author: jsaavedr
"""
import numpy as np
import bw
import basis



#get histogram of an image
def lc_getHistogram(gray_im, rows_cols):
    h=np.zeros(256, dtype=np.float32)
    rows = [p[0] for p in rows_cols]
    cols = [p[1] for p in rows_cols]
    lst_grays=gray_im[rows, cols]
    for gray in lst_grays:
            h[gray]+=1.0
    return h

#contrast enhancement 
def getLevelSet(gray_im, lambda_0, lambda_1):
    inds=np.where((gray_im>=lambda_0) & (gray_im < lambda_1))
    return (inds[0], inds[1])

#
def eq_level_set(im, lambda_0, lambda_1):
    inds=getLevelSet(im, lambda_0, lambda_1)
    print("n {}".format(len(inds[0])))
    bw_im=np.zeros(im.shape, np.uint8)
    bw_im[inds[0], inds[1]]=1
    ccomponents=bw.get_ccomponents(bw_im)
    for cc in ccomponents:
        inds=cc['points']
        h=lc_getHistogram(im, inds)
        n=len(inds)        
        if n>0:
            h=h/float(n)    
            h[h>0.2]=0.2 # clipping
            accum=basis.get_accum(h)
            color_map={}
            for color in  range(int(lambda_0), int(lambda_1)):
                color_map[color]=int(accum[color]*((lambda_1-1)-lambda_0) + lambda_0)
                if (color_map[color]<lambda_0) or  (color_map[color]>lambda_1) :
                    print('ERROR {} {} {} {} {} -----------------------------------------'.format(lambda_0, lambda_1, color, color_map[color], accum[color]))
                #print('{}->{}'.format(color,color_map[color]))
            n=len(inds)
            for i in range(n):
                pos_i=inds[i][0]
                pos_j=inds[i][1]
                im[pos_i, pos_j]=color_map[im[pos_i, pos_j]]
    return basis.to_uint8(im)

#
def local_eq(gray_im):
    imeq=gray_im.copy()
    for i in range(3):
        for j in range(2**i):
            lambda_0=round(256*j/(2**i))
            lambda_1=round(256*(j+1)/(2**i))
            print('l1 {} {}'.format(lambda_0, lambda_1))
            imeq=eq_level_set(imeq, lambda_0, lambda_1)
    return imeq    



    