# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: myDriver.py
# @time: 2020/11/11 8:53
# @desc:
import time

from selenium import webdriver
from 标准云项目.mySetting import url, driverPath, cookies
class Driver:
    driver = None
    def get_driver(self, browser_name = 'Chrome'):
        if self.driver is None:
            if browser_name == 'Chrome':
                self.driver = webdriver.Chrome(driverPath['Chrome'])
            elif browser_name == 'Firefox':
                self.driver = webdriver.Firefox(driverPath['Firefox'])
            # 最大化窗口
            self.driver.maximize_window()
            # 请求网址
            self.driver.get(url)
            # 登录
            self.get_login()
            # 页面刷新
            self.driver.refresh()
        return self.driver
    # 使用登录后的cookie实现免登陆
    def get_login(self):
        #self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
if __name__ == '__main__':
    flogin = Driver()
    flogin.get_driver()