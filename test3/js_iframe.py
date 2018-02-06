#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# profileDir路径对应直接电脑的配置路径
profileDir = r'C:\Users\123\AppData\Roaming\Mozilla\Firefox\Profiles\cr0ic2ar.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)

bolgurl = "http://www.cnblogs.com/"
yoyobolg = bolgurl + "cyfyywfc"
driver.get(yoyobolg)
driver.find_element_by_id("blog_nav_newpost").click()

time.sleep(5)
edittile = u"Selenium2 + python"
editbody = u"这里是发帖的正文"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)


body = "这里是通过js发的正文内容"

# js处理iframe问题(js代码太长了，我分成两行了)
js = 'document.getElementById("Editor_Edit_EditorBody_ifr")' \
     '.contentWindow.document.body.innerHTML="%s"' % body
driver.execute_script(js)
# 保存草稿
driver.find_element_by_id("Editor_Edit_lkbDraft").click()

# 关闭浏览器
driver.quit()
