#-*-coding: utf-8-*-
import os
from collections import Counter

Path = r'C:\Users\zengshuai\Desktop\Test\\'#路径

list = os.listdir(Path)

for dir in list:
    with open(Path+dir,'r') as f:
        t = f.readlines()
        text = ''.join(t)
        texts = text.split()
        l = []
        for word in texts:
            if word.isalpha():
                l.append(word)
        count = Counter(l)
        max = 0
        important = ''
        for k,v in count.items():
            if v>max:
                max = v
                important = k
        print('重要单词：',important)