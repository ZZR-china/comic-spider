# -*- coding: utf-8 -*-
"""
Created on 20201225

@author: ZZR
"""
from ImageCrawlProcess import ImageCrawl as IC

                
if __name__=="__main__":
    url = input("请输入url：")
    craw = IC()
    craw.getImage(url)