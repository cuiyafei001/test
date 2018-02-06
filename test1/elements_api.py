# _*_ coding: UTF-8 _*_
from selenium import webdriver
import random
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()

driver.find_element_by_id("kw").send_keys(u"测试部落")
time.sleep(1)
# submit()模拟enter键提交表单
driver.find_element_by_id("kw").submit()
time.sleep(2)
s = driver.find_elements_by_css_selector("h3.t>a")
# print s
# for i in s:
#     print i.get_attribute("href") # href(链接) 打印出获取到的URL

# 设置随机数
t = random.randint(0, 9)
# print t
# 随机取一个结果点击鼠标
s[t].click()

# 随机取一个结果获取url地址
# a = s[t].get_attribute("href")
# print a
# 这种方式类似接口测试了模拟用户用click方法
# driver.get(a)

time.sleep(2)
driver.quit()
