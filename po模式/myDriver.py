from selenium import webdriver
from po模式.mySetting import driverPath, DOMAIN
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
        if cls._driver is None:
            if browser_name == 'Chrome':
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == 'Firefox':
                cls._driver = webdriver.Chrome(driverPath['Firefox'])
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的网页
            cls._driver.get(DOMAIN)
        return cls._driver

