# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: myDriver.py
# @time: 2020/11/17 10:01
# @desc:
from appium import webdriver
from appium作业2.mySetting import caps
class Driver:
    driver = None
    def get_driver(self):
        if self.driver == None:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        return self.driver
if __name__ == '__main__':
    Driver().get_driver()