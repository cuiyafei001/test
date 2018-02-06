# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
time.sleep(2)
# 切换iframe
# iframe = driver.find_element_by_tag_name("iframe")
# driver.switch_to_frame(iframe)

# 切换iframe 代码划横线的原因水语法过时了，不过还可以用新的应该这么写
# driver.switch_to.frame("x-URS-iframe")
driver.switch_to_frame("x-URS-iframe")
# time.sleep(2)
driver.find_element_by_name("email").send_keys("csliyi001")
driver.find_element_by_name("password").send_keys("110120119.com")

# driver.find_element_by_id("dologin").click()
# driver.find_element_by_xpath(".//*[@id='auto-id-1510905807788']").click()

# 释放iframe，重新回到主界面上
driver.switch_to_default_content()

