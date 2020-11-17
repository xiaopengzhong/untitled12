# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: projectManager.py
# @time: 2020/11/6 15:50
# @desc:
"""
项目管理页面
"""
from selenium.webdriver.common.by import By

from day7.pages.basePage import BasePage
from day7.util.mySettings import url


class ProjectManager(BasePage):
    def __init__(self):
        super().__init__()
        self.url = url
        # 以下封装页面元素寻找方法
        # 项目状态搜索选择下拉框
        self.project_status_locator = (By.NAME, 'status')
        # 项目名称搜索输入框
        self.project_name_input_locator = (By.CSS_SELECTOR, 'form>input')
        # 搜索按钮
        self.search_button_locator = (By.CSS_SELECTOR, 'form>button.btn.btn-primary')
        # 新建项目按钮
        self.create_project_button_locator = (By.CSS_SELECTOR, 'a.btn.btn-success')
        # 匹配列表中的每一个项目名称
        self.list_of_project_locator = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(1)')
        # 匹配列表当中的每一个项目别名
        self.list_of_project_another_name_locator = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(2)')
    def to_page(self):
        """
        访问此页面的网址
        :return:
        """
        self.driver.get(self.url)
    def project_name_input_box(self):
        """项目名称搜索输入框"""
        return self.get_element(self.project_name_input_locator)
    def search_button_box(self):
        """搜索按钮"""
        return self.get_element(self.search_button_locator)
    def list_of_project_name_boxes(self):
        """匹配列表当中的每一个项目名称，返回元素列表"""
        return self.get_elements(self.list_of_project_locator)
    def list_of_project_another_name_boxes(self):
        return self.get_elements(self.list_of_project_another_name_locator)
class ProjectManagerAction(ProjectManager):
    pass
PMA = ProjectManagerAction()



