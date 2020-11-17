# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: loginpage.py
# @time: 2020/11/11 9:08
# @desc:
import time
from selenium import webdriver
"""
获取登录后的cookie
"""
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.standard.jinzhicloud.com/#/login')
# 输入帐号
driver.find_element_by_css_selector('div:nth-child(1) > form > div:nth-child(2) > input[type=text]').send_keys('18319218700')
# 输入密码
driver.find_element_by_css_selector('div:nth-child(1) > form > div:nth-child(3) > input[type=password]').send_keys('123456')
# 在10秒内手动输入验证码
time.sleep(10)
driver.find_element_by_css_selector('div.ivu-tabs-content.ivu-tabs-content-animated > div:nth-child(1) > form > input').click()
time.sleep(1)
print(driver.get_cookies())
