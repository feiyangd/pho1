# -*- coding: utf-8 -*-
from urllib import request  
from  bs4 import BeautifulSoup  
import re  
import time  
  
url = "http://hq.sinajs.cn/list=sh601939"  
html = request.urlopen(url).read() 
#soup = BeautifulSoup(html,'html.parser')  
#print(soup.prettify())  
  
#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句  
#links = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))  
print(html)  
soup = BeautifulSoup(html,'html.parser')  
#print(soup.get_text())
uuu=str(html)
lis1=uuu.split(',')
print(lis1[3])
