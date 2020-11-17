# -*- coding:utf-8 -*-
# @author: zhong
# @project:untitled11
# @file: appium_work1.py
# @time: 2020/11/13 10:56
# @desc:这是boss直聘app
import time
from appium import webdriver
# 准备自动化配置信息
desired_caps ={
    # 移动设备平台
    'platformName': 'Android',
    # 平台OS版本号，写整数位即可
    'platformVersion': '9',
    # 设备的名称，值可以随便写
    'deviceName': 'xiaomi',
    # 提供被测app的信息-包名，入口信息：
    # 1.打开被测app,2.命令行输入以下信息：# adb shell dumpsys activity | findstr intent={
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': '.module.launcher.WelcomeActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒，默认60秒
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName': 'UiAutomator2',  # 或者UiAutomator1
    'skipServerInstallation': True,  # 跳过UI2的安装，如果第一次运行程序，不要添加该配置
}
# 需要知道appium-server地址
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 设置隐式等待时间
driver.implicitly_wait(10)
# 搜索职位信息
# 1.点击搜索
eles = driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')
# 找到第二个元素--放大镜
btn = eles[1]
btn.click()
# 搜索框输入职位信息
search_input = driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
# 输入参数
search_input.send_keys('软件测试')
# 等待关键字输入完毕
time.sleep(2)
# 模拟直接输入enter,66代表回车键
driver.keyevent(66)
# 获取当前页面4个职位信息元素
job_msg = driver.find_elements_by_id('com.hpbr.bosszhipin:id/boss_job_card_view')
for i in range(4):
    job = job_msg[i]
    # 输出岗位名称
    name = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    # 输出薪资
    salary = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    # 输出公司名称
    company = job.find_element_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    print(f'岗位名称：{name.text},薪资：{salary.text},公司简称：{company.text}')

