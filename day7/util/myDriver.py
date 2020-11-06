# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: myDriver.py
# @time: 2020/11/6 11:46
# @desc:
from selenium import webdriver
from day7.util.mySettings import url, cookiesli, driverPath
class Driver:
    # driver默认为空, 若不为空则不创建,直接返回
    driver = None
    def get_driver(self, driver_name = 'Chrome'):
        if Driver.driver is None:
            if driver_name == 'Chrome':
                Driver.driver = webdriver.Chrome(driverPath['Chrome'])
            elif driver_name == 'Firefox':
                Driver.driver = webdriver.Firefox(driverPath['Firefox'])
            # 最大化窗口
            Driver.driver.maximize_window()
            # 请求网址
            Driver.driver.get(url)
            # 登录
            Login().get_login()
        return Driver.driver
class Login():
    def get_login(self):
        Driver.driver.delete_all_cookies()
        for cookie in cookiesli:
            Driver.driver.add_cookie(cookie)
        Driver.driver.refresh()
if __name__ == '__main__':
    Driver().get_driver()