# Python Web测试工具(Selenium)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘Key值
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()  # 声明浏览器对象

try:
    browser.get("http://www.baidu.com")
    print(browser)
    # print(browser.page_source)  # 源代码
    input_data = browser.find_element_by_id("kw")  # 通过ID获取元素
    input_data.send_keys("数据分析")  # 输入搜索参数
    input_data.send_keys(Keys.ENTER)  # 输入回车

    wait = WebDriverWait(browser, 10)  # 等待加载
    # 元素加载出，传入定位元组，如(By.ID, 'p')
    wait.until(EC.presence_of_all_elements_located((By.ID, "content_left")))

    print(browser.current_url)  # 输出URL
    print(browser.get_cookie)  # 输出cookies
    print("——"*30)

    input_data.clear()
    input_data.send_keys("你好")  # 输入搜索参数
    button = browser.find_element_by_id("su")
    button.click()
    print(browser.current_url)  # 输出URL
    print(browser.get_cookie)  # 输出cookies
    print("")
finally:
    browser.close()  # 关闭
