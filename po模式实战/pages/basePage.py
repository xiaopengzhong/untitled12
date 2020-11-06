# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: basePage.py
# @time: 2020/11/5 10:40
# @desc:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po模式实战.utils.myDriver import Driver
from po模式实战.utils.mySettings import url, TIMEOUT, POLL_FREQUENCY


class BasePage:
    def __init__(self):
        # 获取浏览器对象
        self.driver = Driver.get_driver()
        self.url = url
    # def __del__(self):
    #     """
    #     构造方法，对象销毁时执行
    #     :return:
    #     """
    #     self.driver.quit()
    def get_element(self, locator):
        """
        根据表达式匹配单个元素
        :param locator:
        :return:
        """
        WebDriverWait(
            self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator)  # 检测元素定位是否可见
        )
        # 返回元素对象，元组传参
        return self.driver.find_element(*locator)
    def get_elements(self, locator):
        """
        根据表达式匹配元素列表
        :param locators:
        :return:
        """
        WebDriverWait(
            self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            # 检测定位的元素是否可见//元素被定为并可见
            EC.visibility_of_element_located(locator)
        )
        # 返回元素列表，元组传参
        return self.driver.find_elements(*locator)
