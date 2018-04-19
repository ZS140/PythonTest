#coding:utf-8
from xml.dom import minidom

import openpyxl
def getData():
    excel = openpyxl.load_workbook('student.xlsx')
    sheet = excel['student']#获取student表
    dic = {}
    for i in sheet.rows:
        data = [cell.value for cell in i]
        dic[data.pop(0)] = data
    return dic
def outData(dic):
    s = '''
        学生信息表
        "id": [名字, 数学, 语文, 英文]
        '''
    dom = minidom.Document()#创建xml文件
    root = dom.createElement('root')#创建节点
    dom.appendChild(root)#在文件中添加节点
    students = dom.createElement('students')#创建节点
    root.appendChild(students)#在根节点中添加节点
    comment = dom.createComment(s)#创建注释
    students.appendChild(comment)#在students子节点中添加comment
    students_text = dom.createTextNode(str(dic))#创建文本节点
    students.appendChild(students_text)#在students中添加文本节点
    with open('student.xml','w',encoding='utf-8') as f:
        dom.writexml(f,indent=" ",addindent="\t",newl="\n",encoding='utf-8')#写入文件
if __name__ == "__main__":
    outData(getData())