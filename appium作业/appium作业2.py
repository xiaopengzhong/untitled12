# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: appium作业2.py
# @time: 2020/11/13 17:00
# @desc:
import os
import time
import pytest
import yaml
from appium import webdriver
from appium作业.mySetting import caps
class Test1:
    def setup_method(self):
        global driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        # 隐式等待
        driver.implicitly_wait(20)
    def read_yml(self):
        with open('conf.yml', 'r', encoding='utf-8') as fp:
            yml_data = yaml.safe_load(fp)['pwd']
            print(yml_data)
            return yml_data
    def write_yml(self, data):
        with open('conf.yml', 'w', encoding='utf-8') as fp:
            yaml_data = yaml.safe_dump(data)
            fp.write(yaml_data)
    def editpwd(self, old, new):
        # 点击‘我的’标签
        ele = driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_tab_4')
        ele.click()
        # 点击右上角‘设置’
        setting = driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings')
        setting.click()
        # 点击帐号与绑定
        account = driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item')
        account.click()
        time.sleep(1)
        # 点击密码设置
        driver.find_element_by_xpath("//*[@text='修改密码']").click()
        # 旧密码
        old_pwd = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old')
        old_pwd.send_keys(old)
        # 新密码
        new_pwd = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new')
        new_pwd.send_keys(new)
        # 确认密码
        conf_pwd = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm')
        conf_pwd.send_keys(new)
        # 点击完成
        driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()
        # 修改后是否回到登录页面
        login_text = driver.find_element_by_class_name('android.widget.TextView').text
        assert login_text == '手机号登录/注册'
        pwd1 = {}
        pwd1['new_pwd'] = old
        pwd1['old_pwd'] = new
        self.write_yml({'pwd': pwd1})

    # 修改密码后重新登录
    def login(self, new_pwd):
        driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
        driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(new_pwd)
        driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()
        time.sleep(10)
    def test_editpwd(self):
        pwd = self.read_yml()
        self.editpwd(pwd['old_pwd'], pwd['new_pwd'])
        self.login(pwd['new_pwd'])
if __name__ == '__main__':
    pytest.main(['appium作业2.py', '-s', '--alluredir=tmp/my_allure_results'])
    os.system(f'allure serve tmp/my_allure_results')



