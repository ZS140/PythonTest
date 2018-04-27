# coding:utf-8
import datetime
import pymysql
import time

import re
from flask import Flask, request, render_template, redirect, url_for

con = pymysql.connect(host='localhost', user='root', password='1402929679zs', db='test', use_unicode=True,
                      charset='utf8')
cur = con.cursor()
try:
    cur.execute('create table todolist(id INT auto_increment PRIMARY Key,tasks VARCHAR (20),times VARCHAR (20))')
except:
    print("该表已存在")
con.commit()
app = Flask(__name__)


def in_mysql(task, time):#插入数据到数据库
    cur.execute('insert into todolist(tasks,times) VALUES (%s,%s)', [task, time])
    con.commit()


def get_mysql():#从数据库获取数据
    cur.execute('select * from todolist')
    msg = cur.fetchall()
    return msg
def create_page(msg):
    msg = list(msg)
    num = len(msg)
    p = {}
    if num % 5 != 0:
        nums = num // 5 + 1
    else:
        nums = num // 5
    for i in range(nums - 1):
        p[i + 1] = [m for m in msg[i * 5:(i + 1) * 5]]
    p[nums] = msg[(nums - 1) * 5:]
    return p,nums
@app.route('/todo/search',methods = ['POST'])
def search():#搜索任务
    if request.form['search_value']:
        msgs = get_mysql()
        msg = []
        for m in msgs:
            s = re.compile(request.form['search_value'])
            if re.search(s,m[1]):
                msg.append(m)
        if msg:
            p,nums=create_page(msg)
            return render_template('todolist.html',  page=p,page_now = 1,nums = nums)
        else:
            return "不存在该项目"
@app.route('/todo/<task_id>/<int:page_now>')
def del_mysql(task_id,page_now):#删除任务
    cur.execute("delete from todolist WHERE id = %s", task_id)
    return redirect(url_for('todo',page_now = page_now))

@app.route('/todo/<int:page_now>', methods=['POST', 'GET'])
def todo(page_now):
    if request.method == 'POST':#创建任务
        in_mysql(request.form['task'], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return redirect(url_for('todo',page_now=page_now))
    else:#初始页面
        msg = get_mysql()
        if msg:
            p,nums = create_page(msg)
            if page_now >nums:
                page_now-=1
            return render_template('todolist.html', page=p,page_now = page_now,nums = nums)
        else:
            return render_template('todolist.html', page=None,page_now = 0, msgs=None)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8090, debug=True)
