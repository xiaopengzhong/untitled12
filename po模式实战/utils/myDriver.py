# -*- coding:utf-8 -*-
"""
@author: zhong
@file: myDriver.py
@time: 2020/11/5 10:30
@desc: 
"""
from selenium import webdriver
from po模式实战.utils.mySettings import driverPath, url, cookiesli
class Driver:
    # 初始化为None
    _driver = None
    @classmethod
    def get_driver(cls, browser_name='Chrome'):
        """
        获取浏览器对象
        :param browser_name:
        :return:
        """
        # 如果不为空就不需要创建了
        if cls._driver is None:
            if browser_name == 'Chrome':
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的网页
            cls._driver.get(url)
            cls.__login()
            # 刷新页面
            cls._driver.refresh()

        # 返回浏览器驱动对象
        return cls._driver
    @classmethod
    def __login(cls):
        """
        私有方法，只能在类里边使用
        类外部无法使用，子类不能继承
        解决登录问题
        :return:
        """
        # 清除所有cookie
        cls._driver.delete_all_cookies()
        for cookie in cookiesli:
            cls._driver.add_cookie(cookie)
if __name__ == '__main__':
    Driver.get_driver()

