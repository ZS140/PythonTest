#-*-coding:utf-8-*-
from collections import Counter

with open(r'C:\Users\zengshuai\Desktop\Test\text.txt','r') as file:#打开文本文件
    s = file.readlines()#读取文本数据生成列表
    ss = ''.join(s)#连接列表数据
    sss = ss.split()#将字符串分割
    print(s)
    l = []
    for word in sss:
        if word.isalpha():#判断单词是否全由字母组成
            l.append(word)
    count = Counter(l)
    print(count)