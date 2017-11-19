# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
# 打开网易163邮箱
driver.get("http://mail.163.com/")
time.sleep(1)
#切换iframe
driver.switch_to_frame("x-URS-iframe")
time.sleep(1)

# 输入账号密码
driver.find_element_by_name("email").send_keys("cuiyafei001")
driver.find_element_by_name("password").send_keys("110120119.com/.,")
# 点击登录按钮
driver.find_element_by_id("dologin").click()






