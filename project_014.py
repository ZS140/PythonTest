#coding:utf-8
import json

import openpyxl as openpyxl
import xlsxwriter as xlsxwriter

with open('student.txt','r') as f:#打开文本文件
    text = ""
    for line in f:
        text += line
    text = json.loads(text)#采用json加载，用loads()方法加str类型的数据转换成dict
workbook = openpyxl.Workbook()#创建excl
sheet = workbook.create_sheet('student')#创建一个表
cells = sheet.cell#获取表的单元格对象
row = 1#设置初始值
for k,v in text.items():#循环遍历字典类型数据
    cells(row,1).value = k#通过行列为单元格赋值
    col = 2
    for i in v:
        cells(row,col).value = i
        col += 1
    row += 1
workbook.save('student.xlsx')#保存