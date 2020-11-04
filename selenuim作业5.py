from selenium import webdriver
class Page:
    def __init__(self):
        self.driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8088/login")
    # 抽离出浏览器元素控件
    def name(self):
        return self.driver.find_element_by_name("username")  # 用户名
    def password(self):
        return self.driver.find_element_by_name("password")  # 密码
    def login_input(self):
        return self.driver.find_element_by_css_selector("button.btn.btn-lg.btn-login.btn-block")  # 登录
# 抽离出页面动作类, 继承对应的页面类
class LoginPageAction(Page):
    def search(self):
        self.name().send_keys('libai')
        self.password().send_keys("opmsopms123")
        self.login_input().click()
if __name__ == '__main__':
    LoginPageAction().search()

