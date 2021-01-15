#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 实现图片转彩色字符
"""
Created on Fri Aug  4 15:47:07 2017
@author: no1
"""

import argparse
import cv2
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument('--file', default='model.jpg')

args = parser.parse_args()
imgpath = args.file

ascii_char = ['*','/',',','.',' ']

def select_ascii_char(r, g, b): 
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16) 
    unit = 256.0/len(ascii_char) 
    return ascii_char[int(gray/unit)]
        
if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(12, 18))
    im = cv2.imread(imgpath) 
    model=cv2.imread('model.jpg')
    # print(im)
    H,B,C = im.shape
    ax.imshow(model)
    for h in range(H):
        for w in range(B): 
            r,g,b=im[h,w,:3]
            txt = select_ascii_char(r,g,b)
            print('text', txt)
            ax.text(w,h,txt,fontsize=0.01)
    plt.axis('off')      
    plt.savefig('1.png')
    plt.show()