from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po模式2.myDriver import Driver
from po模式2.mySetting import TIMEOUT, POLL_FREQUENCY
class BasePage:
    def __init__(self):
        # 获取浏览器对象
        self.driver = Driver.get_driver()
    def get_element(self, locator):
        """
        根据表达式匹配单个元素
        :param locator:
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            # 检测定位的元素是否可见
            EC.visibility_of_element_located(locator))
        # 返回元素对象，元祖传参
        return self.driver.find_element(*locator)
    def get_elements(self,locator):
        """
        根据表达式匹配元素列表
        :param locator:
        :return:
        """
        # 判断元素是否存在
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY).until(
            # 检测定位的元素是否可见//元素被定位并可见
            EC.visibility_of_element_located(locator)
        )
        # 返回元素列表，元祖传参
        return self.driver.find_elements(*locator)