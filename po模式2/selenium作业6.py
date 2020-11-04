from selenium.webdriver.common.by import By
from po模式2.basePage import BasePage
class ManPraPage(BasePage):
    def __init__(self):
        super().__init__()
        self.manpro = (By.CSS_SELECTOR, "ul.js-left-nav>li:nth-child(2)")
    # 项目管理
    def manpro_button_box(self):
        return self.get_element(self.manpro)
class ManProPageAction(ManPraPage):
    # 点击项目管理
    def mana(self):
        self.manpro_button_box().click()
if __name__=='__main__':
    ManProPageAction().mana()

