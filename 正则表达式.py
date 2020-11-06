import os
import re
# str1 = 'abcdefghijkabbac'
# print(re.findall('a', str1))
# .表示匹配某个字符后面的任意一个字符
# print(re.findall('ab.', str1))
# print(re.findall('ab(.)', str1))
# ab*表示a的后面有n个b，n>=0
# print(re.findall('ab*', str1))
# ab+表示a的后面有n个b,n>=1
# print(re.findall('ab+', str1))
# ab+表示a的后面有0个或1个b
# print(re.findall('ab?', str1))
# .*?表示a的后面有0个或1个b
# str2 = '忽如一夜春风来'
# print(re.findall('忽.*?来', str2))
# print(re.findall('忽(.*?)来', str2))
# 贪婪匹配
# print(re.findall('忽.*', str2))
# 懒惰匹配
# print(re.findall('忽.*?', str2))
# .?匹配一个字符
# print(re.findall('忽.?', str2))
# print(re.findall('忽(.?)', str2))
# \w{n}匹配字母，数字，下划线
# str3 = 'abc&*42fdd'
# print(re.findall('\w{2}', str3))
# \W匹配字母、数字、下划线以外的值
# print(re.findall('\W{2}', str3))
# str4 = '''ggddddddddddgghhbmbm  ffbbd f55fvvv
# fgbbbb gg99rv f                 77v44rfv
# v99vvv fvrg'''
# print(re.findall('\s{5}', str4))
# print(re.findall('\S{5}', str4))
# \d匹配数字
# print(re.findall('\d{2}', str4))
# print(re.findall('\D{2}', str4))  # 匹配数字以外的
# ^匹配开头，$匹配结尾
# list1 = ['abcde', 'fffsss', 'dgtbbc']
# list2 = []
# for i in list1:
#     one = re.findall('^abc', i)
#     print(one)
#     list2.append(one)
#     print(re.findall('bbc$', i))
# print(list2)
# re.I不区分大小写
# str5 = 'ABCVCCDFGG'
# print(re.findall('abc', str5, re.I))
# re.S匹配每一行中符合条件的值
# str6 = '''ABCJHFK abchhbbFF
# hhhh PPPP   ggggg   ggv vvvvvv'''
# print(re.findall('ABC(.*?)vvv', str6, re.S))

#