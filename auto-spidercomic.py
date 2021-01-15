# -*- coding: utf-8 -*-
"""
Created on 20201225

@author: ZZR
"""
import sys
from ImageCrawl import ImageCrawl as IC

def downloadComic(url):
  print('==========正在spider url=',url,'的网页==========')
  craw = IC()
  craw.getImage(url)
  craw.getImage(url)
                
if __name__=="__main__":
  # 读取comics.txt中的urls
  urls=[]
  with open('comics.txt','r') as f:
    for line in f:
      # urls.append(line.strip('\n').split(','))
      urls.append(line.strip('\n'))
  print(urls)
  # 循环spider url
  for url in urls:
    downloadComic(url)
