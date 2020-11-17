# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: basepage.py
# @time: 2020/11/11 9:09
# @desc:
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from 标准云项目.myDriver import Driver
from 标准云项目.mySetting import TIMEOUT, POLL_FREQUENCY
class BasePage:
    def __init__(self):
        self.driver = Driver().get_driver()
    def get_element(self, locator):
        """
        根据表达式匹配单个元素
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)
    def get_elements(self, locator):
        """
        根据表达式匹配列表元素
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)
