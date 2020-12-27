# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:28:03 2019

@author: Ziyuan
"""
#导入必要的模块
import requests
from bs4 import BeautifulSoup as BS
import os

#定义一个爬取图片的类
class ImageCrawl(object):
    def download(self,url,filename):
        if  not os.path.exists('pictures'):
            os.makedirs('pictures')
        r = requests.get(url,stream=True)
        with open(filename,"wb") as f:
            for image in r.iter_content(chunk_size=1024):
                if image:
                    f.write(image)
                    f.flush
                        
    def getImage(self,start=1,end=10):
        #定义需要获取的图片的起始页面
        for i in range(start,end+1):
            #浏览每一页地址可发现就最后一个字符不同
            headers = {"user-agent": "Mizilla/5.0"}
            url = 'https://safebooru.donmai.us/posts?page={}'.format(i)
            print(url)
            
            html = requests.get(url, headers=headers).text
            print(html)


            soup = BS(html,'lxml')
                
                
if __name__=="__main__":
    craw = ImageCrawl()
    craw.getImage()