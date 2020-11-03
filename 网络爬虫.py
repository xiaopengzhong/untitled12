import os
import re
import xlwt, xlrd
import requests
files = os.getcwd()
url1 = 'https://www.xs4.cc/3_3806/'
url2 = re.findall('cc/(.*?)/', url1)[0]
req = requests.get(url1)
req.encoding = 'gbk'
# print(req.text)
book_name = re.findall('<h1>(.*?)</h1>', req.text)[0]  # 获取书名
title_name = re.findall('.html">(.*?)</a></dd>', req.text)
# print(title_name)
# for i in title_name:
#     print(i)
# print(title_name)
wanzhi = re.findall(f'<dd><a href="/{url2}/(.*?).html">', req.text)
# print(wanzhi)
dict1 = {}
for i in range(9, len(title_name)):
    dict1[title_name[i]] = f'{url1}{wanzhi[i]}.html'
# for k, v in dict1.items():
#     print(k, v)
#     pass
if not os.path.exists(f'{files}/file1'):  # 如果不存在文件file1，则创建
    os.mkdir(f'{files}/file1')
excel1 = xlwt.Workbook()  # 实例化一个excel
worksheet = excel1.add_sheet('f{book_name}')  # 新建一个sheep
worksheet.write(0, 0, '目录')
worksheet.write(0, 1, '网址')
rows = 1
for k, v in dict1.items():
    worksheet.write(rows, 0, k)
    worksheet.write(rows, 1, v)
    rows += 1
excel1.save(f'{files}/file1/{book_name}.xls')  # 保存excel文件
# 读取excel文件
data1 = xlrd.open_workbook(f'{files}/file1/{book_name}.xls')
sheet1 = data1.sheets()[0]  # 读取文件第一个sheet
# print(sheet1.nrows)  # nrows返回excel中的有效行数
for i in range(1, sheet1.nrows):
    print(sheet1.cell_value(i, 0), sheet1.cell_value(i, 1))  # 获取单元格内容










