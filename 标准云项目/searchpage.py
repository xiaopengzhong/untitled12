# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: searchpage.py
# @time: 2020/11/11 10:57
# @desc:这是一个搜索类
from selenium.webdriver.common.by import By
from 标准云项目.basepage import BasePage
class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        # 搜索框
        self.search_locator = (By.CSS_SELECTOR, 'input.ivu-input.ivu-input-default')
        # 搜索按钮
        self.search_button_locator = (By.CSS_SELECTOR, 'div.searchBtn.pointer.pull-right')
        # 详情按钮
        self.detail_button_locator = (By.CSS_SELECTOR, 'div.operated.pull-right>div:nth-child(1)')
        # 在线阅读按钮
        self.read_button_locator = (By.CSS_SELECTOR, 'div.pull-left.onLinePdf.pointer')
    def search_locator_box(self):
        """搜索框"""
        return self.get_element(self.search_locator)
    def search_button_locator_box(self):
        """搜索按钮"""
        return self.get_element(self.search_button_locator)
    def detail_button_locator_box(self):
        """详情按钮"""
        return self.get_element(self.detail_button_locator)
    def read_button_locator_box(self):
        """在线阅读按钮"""
        return self.get_element(self.read_button_locator)
class SearchPageAction(SearchPage):
    def search_locator_button(self):
        # 输入搜索内容
        self.search_locator_box().send_keys('输水')
        # 点击搜索
        self.search_button_locator_box().click()
        # 点击标准详情
        self.detail_button_locator_box().click()
        # 点击在线阅读按钮
        self.read_button_locator_box().click()
SAP = SearchPageAction()
SAP.search_locator_button()
