#-*-coding:utf-8-*-
import io
import sys
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
soup = BeautifulSoup(open("sina.html",'rb'),'html.parser')
print(soup.get_text())#打印文本
links = soup.find_all('link')#打印链接
for link in links:
    print(link)