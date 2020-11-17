# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: appium作业1.py
# @time: 2020/11/13 15:11
# @desc:
from appium import webdriver
caps = {
    # 移动设备平台
    'platformName': 'Android',
    # 设备平台版本号
    'platformVersion': '9',
    # 设备的名称
    'deviceName': 'xiaomi',
    # 被测app的报名和入口信息
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': 'module.launcher.WelcomeActivity',
    # 确认自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间
    'newCommandTimeout': 6000,
    # 设置底层驱动UiAutomator2
    'automationName': 'UiAutomator2',
    'skipServerInstallation': True
}
# 初始化driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# 隐式等待
driver.implicitly_wait(10)
# 点击放大镜
eles = driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')
eles[1].click()
# 输入搜索职位信息
search_input = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')
# 模拟键盘点击enter
driver.keyevent(66)
# 点击第一个搜索结果
search_first = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
search_first.click()
# 工作地区
work_place = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_location')
# 工作年限
work_years = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_work_exp')
# 学历
qualifications = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_required_degree')
print(f'工作地区：{work_place.text}, 工作年限：{work_years.text}, 学历: {qualifications.text}')


