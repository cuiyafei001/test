# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time
# 定义浏览器为火狐
driver = webdriver.Firefox()
# 定义打开的URL
url = "file:///C:/Users/123/Desktop/radiobox_checkbox.html"
driver.get(url)
# 通过id属性定位选择男
# driver.find_element_by_id("boy").click()
# time.sleep(10)
# 通过id属性定位选择女
# driver.find_element_by_id("girl").click()

# 通过id定位全选
# driver.find_element_by_id("c1").click()
# driver.find_element_by_id("c2").click()
# driver.find_element_by_id("c3").click()

# 通过xpath定位一个元组来操作
# checkboxs = driver.find_elements_by_xpath(".//*[@type='checkbox']")
# for i in checkboxs:
#     i.click()

# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("boy").is_selected()
print s
driver.find_element_by_id("boy").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("boy").is_selected()
print r


time.sleep(3)
driver.quit()