# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:28:03 2019

@author: Ziyuan
"""
#导入必要的模块
import requests
from bs4 import BeautifulSoup as BS
import os
import sys


headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

#定义一个爬取图片的类
class ImageCrawl(object):
    def download(self,url,filename,picname):
        if  not os.path.exists(filename):
            os.makedirs(filename)
        
        if os.path.exists(picname):
            print('该文件已下载')
            pass
        else:
            r = requests.get(url,stream=True)
            with open(picname,"wb") as f:
                for image in r.iter_content(chunk_size=1024):
                    if image:
                        f.write(image)
                        f.flush

                        
    def getImage(self, url):
        # url = 'https://zhb.doghentai.com/g/341161/list2/'
        # url = url
        
        html = requests.get(url, timeout=10000, headers=headers).text
        soup = BS(html,'lxml')

        allImg = soup.find_all('img',class_='list-img')

        img1 = allImg[1]
        attrs1 = img1.attrs
        alt1 = attrs1['alt']
        fileName = alt1.replace(" - Picture 1", "", 1)
        fileName = fileName.replace("/", " ", 1)

        print(fileName)

        for img in allImg:
            attrs = img.attrs
            dataSrc = attrs['src']
            # 获取文件后缀，如果是svg则不下载
            filestr = dataSrc.split('.')[-1]

            if filestr == 'svg':
                pass
            else:
                picname = os.path.join(fileName, dataSrc.split('/')[-1])
                print(picname)
                self.download(dataSrc,fileName,picname)
                
                
if __name__=="__main__":
    url = input("请输入url：")
    # print(url)
    craw = ImageCrawl()
    craw.getImage(url)