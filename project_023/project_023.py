#coding:utf-8
import time

import pymysql
from flask import Flask, render_template, request, redirect, url_for, abort

con = pymysql.connect('localhost',user='root',password='1402929679zs',db='test',use_unicode = True,charset ="utf8")
cur = con.cursor()
try:
    cur.execute('create table form(id INT auto_increment PRIMARY KEY,user_names VARCHAR (100),times VARCHAR (100),texts VARCHAR (100)) ')
except Exception as e:
    print(e)
    print("该表已存在")

app = Flask(__name__)
def get_mysql():
    cur.execute('SELECT * FROM form ')
    msgs = cur.fetchall()
    con.commit()
    return msgs
def insert_mysql(name,time,text):
    cur.execute('insert into form (user_names,times,texts) VALUES (%s,%s,%s)',[name,time,text])
    con.commit()
@app.route('/',methods=['POST','GET'])
def form():
    if request.method == 'POST':
        name = request.form['first_name']
        times = "留言于（" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "）"
        text = request.form['text']
        insert_mysql(name, times, text)
        msgs = get_mysql()
        return render_template('myform.html', msgs=msgs)
    else:
        msgs = get_mysql()
        if msgs:
            return render_template('myform.html',msgs = msgs)
        else:
            return render_template('myform.html', msgs=None)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8090, debug=True)
