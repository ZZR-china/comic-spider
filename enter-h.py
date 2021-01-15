# -*- coding: utf-8 -*-
"""
Created on 20201225

@author: ZZR
"""
from ImageCrawl import ImageCrawl as IC

                
if __name__=="__main__":
    url = input("请输入url：")
    # print(url)
    craw = IC()
    # 运行两次
    craw.getImage(url)
    craw.getImage(url)