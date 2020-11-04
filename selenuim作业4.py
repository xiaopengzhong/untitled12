import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://localhost:8088/login")
# 帐号
driver.find_element_by_name("username").send_keys('libai')
# 密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 点击登录
driver.find_element_by_css_selector("button.btn.btn-lg.btn-login.btn-block").click()
# 点击项目管理
driver.find_element_by_css_selector("ul.js-left-nav>li:nth-child(2)").click()
time.sleep(1)
# 点击新建项目
# ele = driver.find_element_by_css_selector("section>div>.page-heading>div")
# ActionChains(driver).click(ele).perform()
driver.find_element_by_css_selector("section>div>.page-heading>div").click()
# 项目名称
time.sleep(0.5)
driver.find_element_by_css_selector("form>div:nth-child(1)>div>input").send_keys("selenuim项目")
# 项目别名
driver.find_element_by_css_selector("form>div:nth-child(2)>div>input").send_keys("selenuim项目别名")
# 开始时间
started = driver.find_element_by_name("started")
started.send_keys(Keys.CONTROL, 'a')
started.send_keys(Keys.BACK_SPACE)
started.send_keys("2020-11-01")
# 结束时间
ended = driver.find_element_by_name("ended")
ended.send_keys(Keys.CONTROL, 'a')
ended.send_keys(Keys.BACK_SPACE)
ended.send_keys("2020-11-11")
# 定位iframe标签
iframe = driver.find_element_by_css_selector(".ke-edit-iframe")
# 切换到iframe标签
driver.switch_to.frame(iframe)
# 输入描述
driver.find_element_by_css_selector(".ke-content").send_keys("这是一个描述")
# 回到主页面
driver.switch_to.default_content()
time.sleep(0.5)
# 点击提交
driver.find_element_by_css_selector("button.btn.btn-primary").click()

