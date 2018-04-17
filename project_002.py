#-*-coding:utf-8-*-
import mysql.connector
import random

count = 200
size = 20
code_list = []
for i in range(10):#将数字0~9添加到列表
    code_list.append(str(i))
for i in range(65, 91):#将大写字母添加到列表
    code_list.append(chr(i))
for i in range(97, 123):#将小写字母添加到列表
    code_list.append(chr(i))

conn = mysql.connector.connect(user='root',password='1402929679zs',database='test')#连接数据库
cursor = conn.cursor()

#创建优惠码表
cursor.execute('create table if NOT EXISTS Code(id VARCHAR (20) PRIMARY key,code VARCHAR (20))')
for i in range(200):
    myslice = random.sample(code_list, size)  # 获取列表中size长度的随机序列
    code = ''.join(myslice)
    cursor.execute('insert into Code(id,code)VALUES (%s,%s)',[i+1,code])
conn.commit()#提交事务
cursor.close()#关闭游标
