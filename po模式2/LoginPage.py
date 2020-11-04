from selenium.webdriver.common.by import By
from po模式2.basePage import BasePage
class LoginPage(BasePage):
    def __init__(self):
        """
        进一步抽离元素定位的方法，不会整的去找元素
        """
        # 执行父类的初始化方法
        super().__init__()
        # 用户名输入框
        self.username_input_locator = (By.NAME, "username")
        # 密码输入框
        self.password_input_locator = (By.NAME, "password")
        # 登录按钮
        self.login_button_locator = (By.TAG_NAME, "button")
    # 用户名输入框
    def username_input_box(self):
        return self.get_element(self.username_input_locator)
    def password_input_box(self):
        return self.get_element(self.password_input_locator)
    # 登录按钮
    def login_button_box(self):
        return self.get_element(self.login_button_locator)
# 抽离出页面动作类，继承对应的页面类
class LoginPageAction(LoginPage):
    """
    访问opms登录界面，登录用户
    """
    def login(self):
        # 输入用户名
        self.username_input_box().send_keys("libai")
        # 输入密码
        self.password_input_box().send_keys("opmsopms123")
        # 点击登录按钮
        self.login_button_box().click()
        # self.driver.quit()
if __name__ == '__main__':
    LoginPageAction().login()


