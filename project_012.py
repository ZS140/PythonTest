#coding:utf-8
import re
def filter(words):
    with open('filtered_words.txt','r') as f:
        filtered_words = f.readlines()
        result = words
        for w in filtered_words:
            w = w.strip('\n')
            if re.search(w,words):
                l = len(w)
                result = re.sub(w,"*"*l,result)
        return result
def enter():
    words = input("输入一段话\n")
    result = filter(words)
    print(result)
if __name__ == '__main__':
   enter()