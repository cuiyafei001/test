#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time

driver = webdriver.Ie()
driver.get("https://www.baidu.com")
# 定位百度输入框
driver.find_element_by_id("kw").send_keys("python")

