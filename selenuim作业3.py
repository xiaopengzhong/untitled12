import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(r"D:\code\zjg\GDJZ\Selenium\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.51job.com/")
driver.find_element_by_css_selector("a.more").click()  # 点击【高级搜索】
driver.find_element_by_css_selector("p>input#kwdselectid").send_keys("python")  # 输入搜索关键词Python
time.sleep(0.5)
ActionChains(driver).move_by_offset(200, 100).click().perform()  # 点击空白区,去掉搜索框下拉关键字
# 判断当前所在位置是否在杭州
ele = driver.find_element_by_css_selector("#work_position_input")  # 当前定位城市
if ele.text != '杭州':
    ele.click()
    driver.find_element_by_css_selector("em#work_position_click_ip_location_000000_030200").click()  # 取消当前城市
    driver.find_element_by_css_selector("em#work_position_click_center_right_list_category_000000_080200").click()  # 选择杭州
    driver.find_element_by_css_selector("span#work_position_click_bottom_save").click()  # 点击【确定】
driver.find_element_by_css_selector("span#funtype_click").click()  # 点击【职能类别】
driver.find_element_by_css_selector("em#funtype_click_center_right_list_category_0100_0100").click()  # 点击【后端开发】
driver.find_element_by_css_selector("em#funtype_click_center_right_list_sub_category_each_0100_0106").click()  # 点击【高级工程师】
driver.find_element_by_css_selector("span#funtype_click_bottom_save").click()  # 点击【确定】
driver.find_element_by_css_selector("#workyear_list").click()  # 点击【工作年限】下拉框
driver.find_element_by_css_selector("#workyear_list>.ul>span:nth-child(3)").click()  # 选择工作年限为1-3年
driver.find_element_by_css_selector(".p_sou>.p_but").click()  # 点击【搜索】
if not(driver.find_elements_by_css_selector("div.j_joblist>.e")):  # 搜索不到职位的处理
    print("无搜索结果")
positiong_list = driver.find_elements_by_css_selector("div.j_joblist>.e")  # 搜索结果
# print(positiong_list)
for i in positiong_list:
    positiong_name = i.find_element_by_css_selector(".el>.t>span:nth-child(1)").text  # 职位
    company_name = i.find_element_by_css_selector(".er>a.cname.at").text  # 公司名称
    area = i.find_element_by_css_selector(".el>.info>span.d.at").text  # 发布地区
    palce = area.split('|')[0].strip()
    salary = i.find_element_by_css_selector(".el>.info>span.sal").text  # 薪水
    pub_date = i.find_element_by_css_selector(".el>.t>span:nth-child(2)").text  # 发布时间
    pubulish_date = pub_date[:-2]
    print(f"{positiong_name}|{company_name}|{palce}|{salary}|{pubulish_date}")