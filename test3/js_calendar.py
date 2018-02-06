#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")

# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js)

# 清空文本输入框
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2018-02-01")

# 用JS方法输入日期
js_value = 'document.getElementById("train_date").value="2018-02-01"'
driver.execute_script(js_value)
# 关闭浏览器
# driver.quit()

