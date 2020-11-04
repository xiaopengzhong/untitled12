from selenium import webdriver
from po模式2.mySetting import driverPath, DOMAIN
class Driver:
    _driver = None
    @classmethod
    def get_driver(cls, browser_name='Chrome'):
        """
        获取浏览器对象
        :param browser_name:
        :return:
        """
        # 如果不为空就不需要新建了
        if cls._driver == None:
            if browser_name == 'Chrome':
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            if browser_name == 'Firefox':
                cls._driver = webdriver.Firefox(driverPath['Firefox'])
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的页面
            cls._driver.get(DOMAIN)
            cls.cookie()
        return cls._driver
    # 免登陆方法
    @classmethod
    def cookie(cls):
        c = [{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/',
              'secure': False, 'value': '1604475313'},
             {'domain': '127.0.0.1', 'expiry': 1636011313, 'httpOnly': False,
                                                        'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/',
                                                        'secure': False, 'value': '1604475313'},
             {'domain': '127.0.0.1', 'expiry': 1636011312.93809, 'httpOnly': True, 'name': 'beegosessionID',
              'path': '/', 'secure': False, 'value': '2f9cfb9e27a73c10db2cb1f7a68ec6a7'}]
        # 清除登录前cookie
        cls._driver.delete_all_cookies()
        # 添加cookie
        for i in c:
            cls._driver.add_cookie(i)
        # 刷新页面
        cls._driver.refresh()