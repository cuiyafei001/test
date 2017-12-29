# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(2)

title = driver.title
print title
text = driver.find_element_by_id("setf").text
print text
# 获取元素的标签
tag = driver.find_element_by_id("kw").tag_name
print tag
# 获取元素的其他属性
name = driver.find_element_by_id("kw").get_attribute("class")
print name
# 回去输入框的内容
driver.find_element_by_id("kw").send_keys("python+selenium  good good good a very good")
value = driver.find_element_by_id("kw").get_attribute("value")
print value
# 获取浏览器名称.
print driver.name

driver.quit()