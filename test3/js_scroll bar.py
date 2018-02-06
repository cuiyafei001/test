#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time

dr = webdriver.Firefox()
dr.get("http://www.cnblogs.com/cyfyywfc/")
# dr.maximize_window()

# JS滚动条拉到底部
js = "var q = document.documentElement.scrollTop=10000"
dr.execute_script(js)
time.sleep(5)
# 滚动条拉到顶部
js = "var q = document.getElementById('id').scrollTop=0"
# scrollTo(x,y)
# js = "windows.scrollTo(100,400);"
dr.execute_script(js)

# 聚焦元素
target = dr.find_element_by_id("blog_nav_newpost")
dr.execute_script("arguments[0].scrollIntoView();",target)

