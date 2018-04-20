#coding:utf-8
from xml.dom import minidom

import openpyxl

excel =  openpyxl.load_workbook('city.xlsx')#加载Excel表
sheet = excel["city"]#获取表对象
dic = {}
for i in sheet.rows:#循环遍历表的每一行
    col = [cell.value for cell in i]
    dic[col.pop(0)] = col
dom = minidom.Document()#创建xml文件
root = dom.createElement('root')#创建根节点
cities = dom.createElement('cities')#创建节点
coment = dom.createComment('城市信息')
text = dom.createTextNode(str(dic))
dom.appendChild(root)#将节点添加到xml中
root.appendChild(cities)
cities.appendChild(coment)
cities.appendChild(text)
with open('city.xml','w+',encoding='utf-8') as f:#写入文件
    dom.writexml(f,addindent='  ',newl='\n',encoding='utf-8')