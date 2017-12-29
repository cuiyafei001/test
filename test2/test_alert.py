# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

url = "file:///C:/Users/123/Desktop/testalert.HTML"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)

# 点击链接里的alert按钮
# driver.find_element_by_id("alert").click()
# 点击链接里的prompt
driver.find_element_by_id("prompt").click()
# 点击链接里的confirm
driver.find_element_by_id("confirm").click()
time.sleep(3)
t = driver.switch_to_alert()

# 打印警告框文本内容
print t.text

# 点警告框确认按钮
# t.accept()
# t.dismiss()相当于点x按钮，取消
# t.dismiss()
# 点击prompt用send_keys方法输入"hello selenium2"
t.send_keys("hello selenium2")