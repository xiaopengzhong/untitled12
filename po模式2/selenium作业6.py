from selenium import webdriver

from po模式2.basePage import BasePage

driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.get("http://127.0.0.1:8088")
c = [{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1604475313'}, {'domain': '127.0.0.1', 'expiry': 1636011313, 'httpOnly': False, 'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1604475313'}, {'domain': '127.0.0.1', 'expiry': 1636011312.93809, 'httpOnly': True, 'name': 'beegosessionID', 'path': '/', 'secure': False, 'value': '2f9cfb9e27a73c10db2cb1f7a68ec6a7'}]
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())
for i in c:
    driver.add_cookie(i)
print(driver.get_cookies())
driver.refresh()
print(driver.get_cookies())
class ManPraPage(BasePage):
    def __init__(self):
        super().__init__()
    def manpro_button_box(self):
        self.manpro = ''

