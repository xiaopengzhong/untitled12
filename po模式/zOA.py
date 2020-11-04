from po模式.myDriver import Driver
class LoginPage:
    def __init__(self):
        # 创建driver对象
        self.driver = Driver.get_driver()
    # 用户名输入框
    def username_input_box(self):
        return self.driver.find_element_by_name("username")
    # 密码输入框
    def password_input_box(self):
        return self.driver.find_element_by_name("password")
    # 登录按钮
    def login_button_box(self):
        return self.driver.find_element_by_css_selector("button.btn.btn-lg.btn-login.btn-block")
# 抽离出页面动作类，继承对应的页面类
class LoginPageAction(LoginPage):
    def login(self):
        """
        访问opms登录界面，登录用户
        :return:
        """
        # 输入用户名
        self.username_input_box().send_keys("libai")
        # 输入密码
        self.password_input_box().send_keys("opmsopms123")
        # 点击登录按钮
        self.login_button_box().click()
        print(self.driver.get_cookies())
if __name__=='__main__':
    LoginPageAction().login()
