import re
import time
from selenium import webdriver
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.get("https://m.weibo.cn/")
driver.find_element_by_class_name("m-text-cut").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='card-main']/div[@class='m-item-box'][8]/div[@class='m-diy-btn m-box-col m-box-center0 m-box-center-a']").click()
time.sleep(5)
ele = driver.find_elements_by_xpath("//div[@class='card card11'][1]/div/div[@class='card-list']/div[@class='card m-panel card4']")
for i in ele:
    try:
        photo = i.find_element_by_xpath("./div[@class='card-wrap']/div[@class='card-main']/div[@class='m-box']/div[@class='box-left m-box-col m-box-center-a']/span[@class='main-link m-box m-box-center-a']/span[@class='m-link-icon']/img").get_attribute('src')
        piture = re.findall("_(.*?).png", photo)[0]
        content = i.find_element_by_xpath("./div[@class='card-wrap']/div[@class='card-main']/div[@class='m-box']/div[@class='box-left m-box-col m-box-center-a']/span[@class='main-link m-box m-box-center-a']/span[@class='main-text m-text-cut']").text
        if piture != 'jian':
            print(f'{piture} : {content}')
    except:
        pass
driver.quit()
