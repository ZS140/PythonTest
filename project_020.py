#coding:utf-8
import re

import time
import xlrd
def getData():
    excel = xlrd.open_workbook(r'C:\Users\zengshuai\Desktop\2018年04月语音通信.xls')#读取老版本的Excel（xls后缀）使用xlrd
    sheet = excel.sheet_by_name("2018年04月语音通信")#获取表单对象
    data = []
    for i in sheet.get_rows():#循环读取表单数据
        col = [cell.value for cell in i]
        data.append(col)
    data.remove(data[0])#表单数据第一行为索引，删除第一行
    for i in data:#将通话时长转换为时间格式，方便读取
        s1 = '分'
        s2 = '小时'
        i[3] =  re.sub("秒",'', i[3])
        if re.search(s1,i[3]):
            i[3] = re.sub(s1,':',i[3])
        else:
            i[3] = '00:'+i[3]
        if re.search(s2,i[3]):
            i[3] = re.sub(s2,':',i[3])
        else:
            i[3] = '00:'+i[3]
        i[3] = '0001-01-01 '+i[3]
    return data
def call(datas):
    time_sum1,time_sum2 = 0,0
    for i in datas:
        times = time.strptime(i[3], '%Y-%m-%d %H:%M:%S')
        if i[4] == '被叫':
            time_sum1 += (times.tm_hour*3600+times.tm_min*60+times.tm_sec)
        elif i[4] =='主叫':
            time_sum2 += (times.tm_hour*3600+times.tm_min*60+times.tm_sec)
    return time_sum1,time_sum2
if __name__ == '__main__':
    datas = getData()
    result1,result2 = call(datas)
    print("被叫时间：",result1)
    print("主叫时间：",result2)