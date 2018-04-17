#-*-coding:utf-8-*-
empty_line = 0
code_line = 0
with open('project_005.py','rb') as file:
    for line in file:
        line = line.decode('utf-8')
        if line=='\r\n':
            empty_line += 1
        else:
            code_line+=1
print(empty_line)
print(code_line)