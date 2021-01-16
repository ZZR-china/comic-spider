# -*- coding: utf-8 -*-
"""
Created on 20201225

@author: ZZR
"""
import sys
import threading

from ImageCrawl import ImageCrawl as IC

thread_max_num = threading.Semaphore(10)

def downloadComic(url):
    print('==========正在Spider url=',url,'的网页==========')
    craw = IC()
    craw.getImage(url)

if __name__=="__main__":
    # 读取comics.txt中的urls
    urls=[]
    with open('.\comicsTxts\comics.txt','r') as f:
        for line in f:
            urls.append(line.strip('\n'))
        print(urls)
    # 循环spider url
    # with thread_max_num:
    for url in urls:
        # 单线程下载
        # downloadComic(url)

        # 开启多线程进行下载
        th = threading.Thread(target = downloadComic, args=(url,))
        th.start()

