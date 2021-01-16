# -*- coding: utf-8 -*-
"""
Created on 20210115

@author: ZZR
"""
#导入必要的模块
import time
import random
import requests
from bs4 import BeautifulSoup as BS
import os
import sys
import re
import multiprocessing
from multiprocessing import Pool
from requests.adapters import HTTPAdapter

ress = requests.Session()

# max_retries 为最大重试次数，重试3次，加上最初的一次请求，一共是4次，所以上述代码运行耗时是20秒而不是15秒
ress.mount('http://', HTTPAdapter(max_retries=3))
ress.mount('https://', HTTPAdapter(max_retries=3))

headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

proxies = {'http': 'http://localhost:4780', 'https': 'http://localhost:4780'}

#定义一个爬取图片的类
class ImageCrawl(object):
    def setPic(picname,r):
        with open(picname,"wb") as f:
            for image in r.iter_content(chunk_size=1024):
                if image:
                    f.write(image)
                    f.flush

    def download(self,url,filename,picname,backUpUrl,backUpPicname):
        if  not os.path.exists(filename):
            os.makedirs(filename)
        
        if os.path.exists(picname):
            print('该文件已下载')
            pass
        else:
            try:
                r = ress.get(url,stream=True,timeout=5,proxies=proxies)
                if r.status_code == 404:
                    print('is 404')
                    rb = ress.get(backUpUrl,stream=True,timeout=5,proxies=proxies)
                    with open(backUpPicname,"wb") as f:
                        for image in rb.iter_content(chunk_size=1024):
                            if image:
                                f.write(image)
                                f.flush
                else:
                    with open(picname,"wb") as f:
                        for image in r.iter_content(chunk_size=1024):
                            if image:
                                f.write(image)
                                f.flush
            except requests.exceptions.RequestException as e:
                print(e)

                        
    def getImage(self, url):
        # url = 'https://zhb.doghentai.com/g/341161/list2/'
        html = ress.get(url, timeout=5, headers=headers,proxies=proxies).text
        soup = BS(html,'lxml')

        allImg = soup.find_all('img',class_='list-img')
        # 生成文件夹名
        img1 = allImg[1]
        attrs1 = img1.attrs
        alt1 = attrs1['alt']
        fileName = alt1.replace(" - Picture 1", "", 1)
        fileName = fileName.replace("/", " ", 1)
        fileName = os.path.join('pictrues', fileName)
        # 去除特殊字符
        fileName = re.sub('[!@#$]\/:*?"<>|', '', fileName)
        # 非空判断
        if fileName.strip() == '':
            randomTime = random.randint(1,3)
            fileName = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())) + '-' + str(randomTime)

        print('文件夹名：', fileName)

        allLen = len(allImg) / 2

        print('Parent process %s.' % os.getpid())
        p = Pool(multiprocessing.cpu_count())

        img = allImg[0]

        print('img', img)

        attrs = img.attrs
        dataSrc = attrs['onerror']
        dataSrc = dataSrc.replace("javascript:this.src='", " ", 1)
        dataSrc = dataSrc.replace("';this.onerror = null", " ", 1)
        dataSrc = dataSrc.strip()

        backUpUrl = attrs['data-src']
        #   'https://i0.nyacdn.com/galleries/1110228/1.jpg'
        print('dataSrc:', dataSrc)
        print('backUpUrl:', backUpUrl)
        # 获取文件后缀，如果是svg则不下载
        filestr = dataSrc.split('.')[-1]
        if filestr == 'svg':
            pass
        else:
            picname = os.path.join(fileName, dataSrc.split('/')[-1])
            print('图片名称：', picname, '，共：',allLen,'张')

            backUpPicname = os.path.join(fileName, backUpUrl.split('/')[-1])
            print('备用图片名：', backUpPicname, '，共：',allLen,'张')
            p.apply_async(self.download, args=(dataSrc,fileName,picname,backUpUrl,backUpPicname))

        print('等待所有子进程结束...')
        p.close()
        p.join()
        print('所有子进程结束。')

if __name__=="__main__":
    craw = ImageCrawl()
    craw.getImage('https://zhb.doghentai.com/g/207252/list2/')
    # r = ress.get('https://i0.nyacdn.com/galleries/1110228/1.jpg',stream=True,timeout=5,proxies=proxies)
    # print(r.status_code)