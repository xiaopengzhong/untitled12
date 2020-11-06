# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: basePage.py
# @time: 2020/11/6 15:50
# @desc:
from selenium.webdriver.support.wait import WebDriverWait
from day7.util.myDriver import Driver
from day7.util.mySettings import TIMEOUT, POLL_FREQUENCY
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init(self):
        self.driver = Driver().driver()
    def get_element(self, locator):
        """
        根据表达式匹配单个元素
        :param locator:
        :return:
        """
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)
    def get_elements(self, locator):
        """
        根据表达式匹配列表元素
        :param locator:
        :return:
        """
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(*locator)
        )
        return self.driver.find_elements(*locator)
