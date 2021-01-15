# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:28:03 2019

@author: Ziyuan
"""
#导入必要的模块
import requests
from bs4 import BeautifulSoup as BS
import os

headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

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
        url = 'https://zhb.doghentai.com/g/341161/list2/'
        
        
        html = requests.get(url, timeout=10000, headers=headers).text
        soup = BS(html,'lxml')

        for img in soup.find_all('img',class_='list-img'):
            attrs = img.attrs
            # print(attrs)
            dataSrc = attrs['src']
            # print(dataSrc)

            filename = os.path.join('pictures', dataSrc.split('/')[-1])
            self.download(dataSrc,filename)
                
                
if __name__=="__main__":
    craw = ImageCrawl()
    craw.getImage()