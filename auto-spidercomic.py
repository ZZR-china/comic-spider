# -*- coding: utf-8 -*-
"""
Created on 20201225

@author: ZZR
"""
import logging
import sys
import time
from ImageCrawlProcess import ImageCrawl as IC


def downloadComic(url):
    logging.info('==========正在Spider url=',url,'的网页==========')
    print('==========正在Spider url=',url,'的网页==========')
    craw = IC()
    craw.getImage(url)

if __name__=="__main__":
    time_start=time.time()

    urls=[]
    with open('.\comicsTxts\comics.txt','r') as f:
        for line in f:
            urls.append(line.strip('\n'))

    urls = [x for x in urls if x != '']
    print(urls)

    if len(urls):
        sys.exit()

    for url in urls:
        downloadComic(url)
    
    time_end=time.time()
    print('程序耗时：', time_end-time_start ,'秒')

