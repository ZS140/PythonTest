#coding:utf-8
from xml.dom import minidom

import openpyxl

excel = openpyxl.load_workbook('numbers.xlsx')
sheet = excel['numbers']
list = []
for i in sheet.rows:
    col = [cell.value for cell in i]
    list.append(col)
dom = minidom.Document()
root = dom.createElement('root')
numbers = dom.createElement('numbers')
comment = dom.createComment(' 数字信息')
text = dom.createTextNode(str(list))
dom.appendChild(root)
root.appendChild(numbers)
numbers.appendChild(comment)
numbers.appendChild(text)
with open('numbers.xml','w+',encoding='utf-8') as f:
    dom.writexml(f,addindent="  ",newl="\n",encoding='utf-8')