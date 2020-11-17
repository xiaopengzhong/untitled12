# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: mySetting.py
# @time: 2020/11/11 8:53
# @desc:
# 显示等待超时时间
TIMEOUT = 10
# 显示等待轮询时间
POLL_FREQUENCY = 0.5
# 浏览器驱动路径
driverPath = {
    'Chrome': r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe",
    'Firefox': r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe"
}
# 网址
url = 'https://www.standard.jinzhicloud.com'

# cookie
cookies = [{'domain': 'www.standard.jinzhicloud.com', 'httpOnly': False, 'name': 'logined', 'path': '/', 'secure': False, 'value': '1'},
           {'domain': 'www.standard.jinzhicloud.com', 'expiry': 1607674642, 'httpOnly': False, 'name': 'encryptPw', 'path': '/', 'secure': False, 'value': ''},
           {'domain': 'www.standard.jinzhicloud.com', 'expiry': 1607674642, 'httpOnly': False, 'name': 'userLoginName', 'path': '/', 'secure': False, 'value': ''},
           {'domain': 'www.standard.jinzhicloud.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': True, 'value': '1ABF1393B77C52341067C2BBDEFCB288'}]
