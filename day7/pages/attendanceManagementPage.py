# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: attendanceManagementPage.py
# @time: 2020/11/9 9:52
# @desc:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from day7.pages.basePage import BasePage
from day7.util.mySettings import url
"""
考勤管理页面"""
class AttendanceManagementPage(BasePage):
    def __init__(self, path='/checkwork/manage'):
        """
        考勤管理页面类
        :param path:
        """
        super(AttendanceManagementPage, self).__init__()
        self.url = url + path
        # 以下封装页面元素寻找方法
        # 打卡按钮
        self.sign_button_locator = (By.CSS_SELECTOR, "#js-clock > span")
        # 打卡状态下拉框
        self.sign_status_select_locator = (By.CSS_SELECTOR, "form > select[class=\"form-control\"]")
        # 打卡状态搜索按钮
        self.sign_status_search_button_locator = (By.CSS_SELECTOR, "form > select[class=\"form-control\"]+button")
        # 考勤表
        self.sign_table_locator = (By.TAG_NAME, "table")
        # 匹配考勤表的每一行考勤
        self.sign_table_tr_locator = (By.CSS_SELECTOR, "tbody > tr")
        # 匹配考勤表的每一个日期
        self.sign_table_date_locator = (By.CSS_SELECTOR, "tbody td:nth-child(1)")
        # 匹配考勤表的每一个打卡
        self.sign_table_time_locator = (By.CSS_SELECTOR, "tbody td:nth-child(2)")
        # 匹配考勤表的每一个状态
        self.sign_table_status_locator = (By.CSS_SELECTOR, "tbody td:nth-child(3)")
        # 匹配考勤表的每一个ip
        self.sign_table_ip_locator = (By.CSS_SELECTOR, "tbody td:nth-child(4)")
    def to_page(self):
        """访问此页面的网址"""
        self.driver.get(self.url)
    def sign_button_box(self):
        """打卡按钮"""
        return self.get_element(self.sign_button_locator)
    def sign_status_select_box(self):
        """打卡状态下拉框"""
        return self.get_element(self.sign_status_select_locator)
    def sign_status_search_button_box(self):
        """打卡状态搜索按钮"""
        return self.get_element(self.sign_status_search_button_locator)

    def sign_table_box(self):
        """考勤表"""
        return self.get_element(self.sign_table_locator)

    def sign_table_tr_boxes(self):
        """匹配考勤表的每一行考勤"""
        return self.get_elements(self.sign_table_tr_locator)

    def sign_table_date_boxes(self):
        """匹配考勤表的每一个日期"""
        return self.get_elements(self.sign_table_date_locator)

    def sign_table_time_boxes(self):
        """匹配考勤表的每一个打卡"""
        return self.get_elements(self.sign_table_time_locator)

    def sign_table_status_boxes(self):
        """匹配考勤表的每一个状态"""
        return self.get_elements(self.sign_table_status_locator)

    def sign_table_ip_boxes(self):
        """匹配考勤表的每一个ip"""
        return self.get_elements(self.sign_table_ip_locator)
# 页面动作类
class AttendanceManagementPageAction(AttendanceManagementPage):
    def punchClock(self):
        """
        点击打卡按钮
        :return:
        """
        self.sign_button_box().click()
    def signStatusSearch(self, status):
        """
        按打卡状态搜索考勤
        :param status: 状态选择，默认为搜索全部
        :return:
        """
        # 根据可视文本选择下拉框选项
        Select(self.sign_status_select_box()).select_by_visible_text(status)
        # 点击搜索按钮
        self.sign_status_search_button_box().click()
AMPA = AttendanceManagementPageAction()
