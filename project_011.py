#coding:utf-8
import re
def filter(words):
    with open('filtered_words.txt','r') as f:
        filtered_words = f.readlines()
        for w in filtered_words:
            if re.search(w.strip('\n'),words):
                return 'Freedom'
        return 'Human Rights'
def enter():
    words = input("输入一段话\n")
    result = filter(words)
    print(result)
if __name__ == '__main__':
   enter()