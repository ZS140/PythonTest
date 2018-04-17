import io
from urllib import request

import sys
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%F5%D5%DF%C8%D9%D2%AB%B8%DF%C7%E5%CD%BC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'
requestion = request.Request(url,headers=headers)
response = request.urlopen(requestion)
page = response.read()

soup = BeautifulSoup(page,'html.parser')

pic = soup.find_all('img')
print(pic)
for img in pic:
    print(img.get('src'))