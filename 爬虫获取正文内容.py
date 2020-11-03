# 获取内容
import os
import re
import requests
import xlrd
files = os.getcwd()
data2 = xlrd.open_workbook(f'{files}/file1/大唐技师.xls')
sheet = data2.sheets()[0]
for i in range(1, 2):
    req = requests.get(sheet.cell_value(i, 1))
    req.encoding = 'gbk'
    # print(req.text)
    contents = re.findall('<div id="content">(.*?)</div>', req.text, re.S)[0]
    content = contents.replace('<br />', '').replace('&nbsp;', '')
    with open(f'{files}/file1/{sheet.cell_value(i, 0)}.txt', 'w', encoding='utf-8') as fp:
        fp.write(content)
