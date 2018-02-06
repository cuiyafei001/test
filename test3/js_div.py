#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("file:///C:/Users/123/Desktop/js.html")

# 纵向底部
# js1 = 'document.getElementById("yoyoketang").scrollTop=10000'
# driver.execute_script(js1)
# time.sleep(5)

# 纵向顶部
# js2 = 'document.getElementById("yoyoketang").scrollTop=0'
# driver.execute_script(js2)

# 横向右侧
# js3 = 'document.getElementById("yoyoketang").scrollLeft=10000'
# driver.execute_script(js3)
# time.sleep(5)

# 横向左侧
# js4 = 'document.getElementById("yoyoketang").scrollLeft=0'
# driver.execute_script(js4)

# 获取的class返回得失list对象，取list的第一个
js5 = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)
time.sleep(5)

# 控制横向滚动条位置
js6 = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)
time.sleep(5)

# 运行结束关闭浏览器
driver.quit()