from selenium import webdriver
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.vmall.com")
js = "window.scrollTo(800,800);"
driver.execute_script(js)
driver.implicitly_wait(3)
eles = driver.find_elements_by_xpath("//div[@class='span-968 fl']/ul[@class='grid-list clearfix']/li[@class='grid-items']")
print(eles)
for i in eles:
    name = i.find_element_by_xpath(".//p[@class='grid-tips']/em/span").text  # 爆款名称
    price = i.find_element_by_xpath("//div[@class='grid-title']") + i.find_element_by_xpath(".//p[@class='grid-price']").text
    if '爆款' in name:
        print(f'爆款： {name}, 价格： {price}')