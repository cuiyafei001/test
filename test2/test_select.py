# _*_ coding: UTF-8 _*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   # 导入模拟鼠标操作包
from selenium.webdriver.support.select import Select               # 导入select方法
import time

driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)
time.sleep(1)
# 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()

# 分两步：先定位下拉框，再点击选项
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()

# 直接通过xpath定位
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()

# 通过索引：select_by_index(2)
# s = driver.find_element_by_id("nr")
# Select(s).select_by_index(2)

# 通过value：select_by_value()
# s = driver.find_element_by_id("nr")
# Select(s).select_by_value("20")

# 通过text：Select_by_visible_text()
s = driver.find_element_by_id("nr")
Select(s).select_by_visible_text("每页显示20条")
time.sleep(3)
s.click()

# 设置之后点击保存设置按钮
driver.find_element_by_link_text("保存设置").click()
time.sleep(5)

# 获取alert弹框
t = driver.switch_to_alert()
print t.text
t.accept()
time.sleep(3)

driver.quit()