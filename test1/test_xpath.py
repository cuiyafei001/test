# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

# 第二步打开浏览器
driver = webdriver.Firefox()
# 第三步打开百度
driver.get("https://www.baidu.com/")
# 设置休眠时间为3秒，也可以是小数，单位是秒
time.sleep(3)

# 用xpath通过name属性定位
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")

# 用xpath通过class属性定位
# driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("python")

# 用xpath其他属性定位
# driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("python")

# driver.quit()
# 通过xpath它老爸来定位span的属性
# driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("python")

# 通过xpath它爷爷来定位input的属性
# driver.find_element_by_xpath("// form[@id='form']/span/input").send_keys("python")

# xpath逻辑运算
# driver.find_element_by_xpath("//*[@id='kw'and @autocomplete='off']").send_keys("pyrton")

# xpath模糊匹配功能
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()

# xpath模糊匹配某个属性
# driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()

# xpath模糊匹配以什么开头
# driver.find_element_by_xpath("//*[starts-with(@id,'s_menu_m')]").click()

# xpath模糊匹配以什么结尾
# driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()

# xpath支持最强的正则表达式
# driver.find_element_by_xpath("//*[matchs(text(),'hao13')]").click()