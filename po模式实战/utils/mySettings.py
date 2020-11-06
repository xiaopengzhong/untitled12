# -*- coding:utf-8 -*-
"""
@author: 
@file: mySettings.py
@time: 2020/11/5 10:24
@desc: 
"""
# 网址
url = "http://10.10.10.113:8088"
# 超时时间
TIMEOUT = 10
# 轮询时间
POLL_FREQUENCY = 0.5
# 浏览器驱动路径
driverPath = {
    'Chrome': r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe"
    # 填其他更多的
}
# cookie，过期后需要更新
cookiesli = [{'domain': '10.10.10.113', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1604631024'},
             {'domain': '10.10.10.113', 'expiry': 1636167024, 'httpOnly': False, 'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1604631024'},
             {'domain': '10.10.10.113', 'expiry': 1636167023.578724, 'httpOnly': True, 'name': 'beegosessionID', 'path': '/', 'secure': False, 'value': '0571019b254f1ebef8e6322d02e67607'}]


