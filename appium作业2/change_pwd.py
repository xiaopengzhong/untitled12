# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: change_pwd.py
# @time: 2020/11/17 10:09
# @desc:
import os
import time
import pytest
import yaml
from appium作业2.myDriver import Driver
class ChangePwd:
    def __init__(self):
        self.driver = Driver().get_driver()
        self.driver.implicitly_wait(20)
    # 读取yaml文件
    def read_yml(self):
        with open('conf.yml', 'r', encoding='utf-8') as fp:
            yml_data = yaml.safe_load(fp)['pwd']
            return yml_data
    # 写入yaml文件
    def write_yml(self, data):
        with open('conf.yml', 'w', encoding='utf-8')as fp:
            content = yaml.safe_dump(data)
            fp.write(content)
    def editpwd(self, old, new):
        # 点击‘我的’标签
        ele = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_tab_4')
        ele.click()
        # 点击右上角‘设置’
        setting = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings')
        setting.click()
        # 点击帐号与绑定
        account = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item')
        account.click()
        time.sleep(1)
        # 点击密码设置
        self.driver.find_element_by_xpath("//*[@text='修改密码']").click()
        # 旧密码
        old_pwd = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old')
        old_pwd.send_keys(old)
        # 新密码
        new_pwd = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new')
        new_pwd.send_keys(new)
        # 确认密码
        conf_pwd = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm')
        conf_pwd.send_keys(new)
        # 点击完成
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
        # 交换密码
        pwd = {}
        pwd['new_pwd'] = old
        pwd['old_pwd'] = new
        self.write_yml({'pwd': pwd})

    # 修改密码后登录
    def login(self, new_pwd):
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(new_pwd)
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()
        time.sleep(5)
        context = self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_tab_1')
        assert context.text == '职位'

class Test:
    def test_newpwd_login(self):
        ch = ChangePwd()
        pwd = ch.read_yml()
        ch.editpwd(pwd['old_pwd'], pwd['new_pwd'])
        ch.login(pwd['new_pwd'])

if __name__ == '__main__':
    pytest.main(['change_pwd.py', '-s', '--alluredir=tmp/my_allure_results'])
    os.system(f'allure serve tmp/my_allure_results')
