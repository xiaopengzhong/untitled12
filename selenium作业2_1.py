from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.get("https://www.vmall.com/")
driver.implicitly_wait(4)  # 隐式等待
ele_lists = driver.find_elements_by_xpath("//div[@class='b']/ol[@class='category-list']/li")  # 一级菜单列表
for i in ele_lists:
    level1 = i.find_element_by_xpath("./div[@class='category-item-bg']/div/a/span").text  # 一级菜单
    print(f'一级菜单： {level1}')
    above = i.find_element_by_xpath("./div[@class='category-item-bg']")
    ActionChains(driver).move_to_element(above).perform()
    eles = i.find_elements_by_xpath(".//ul/li[@class='subcate-item']")
    # print(eles)
    for j in eles:
        level2 = j.find_element_by_xpath("./a/p/span").text
        print(f'    {level2}')


