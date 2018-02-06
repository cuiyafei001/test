# _*_ coding: UTF-8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# import random
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# driver.get("http://testerhorde.com/")
driver.maximize_window()
time.sleep(1)

# 清空百度输入文本框
# driver.find_element_by_id("kw").clear()
# send_keys里如果是中文的话，前面加u
# driver.find_element_by_id("kw").send_keys(u"小白兔去哪里了")
# driver.find_element_by_id("su").click()
# submit()模拟enter键提交表单
# driver.find_element_by_id("kw").submit()

# #通过id定位属性
# driver.find_element_by_id("search-button").click()
# 清空输入文本框
# driver.find_element_by_id("search-term").clear()
# 输入selenium
# driver.find_element_by_id("search-term").send_keys("selenium")
# 模拟enter键操作回车按钮
# driver.find_element_by_id("search-term").send_keys(Keys.ENTER)

# 进入百度后模拟键盘F12打开web元素
# driver.find_element_by_id("kw").send_keys(Keys.F12)
# 进去百度后模拟Ctrl+a全选
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# 鼠标悬停在设置按钮上
mouse = driver.find_element_by_partial_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# 鼠标右键点击设置按钮
# ActionChains(driver).context_click(mouse).perform()
# 双击鼠标点击设置按钮
ActionChains(driver).double_click(mouse).perform()


time.sleep(2)

# time.sleep(1)
# driver.quit()