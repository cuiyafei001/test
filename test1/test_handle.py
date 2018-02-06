# _*_ coding: UTF-8 _*_
# 第一步打入webdriver模块
from selenium import webdriver
# 导入时间模块
import time

# 第二步打开浏览器
driver = webdriver.Firefox()
# 第三步打开赶集网首页
driver.get("http://bj.ganji.com/")
time.sleep(1)

# 进入赶集网点击首页工作按钮
# driver.find_element_by_css_selector(".dt-t").click()
# time.sleep(1)

# 获取当前窗口句柄
h = driver.current_window_handle
print h      # 打印首页句柄

driver.find_element_by_link_text("工作").click()
time.sleep(1)

# 获取所有窗口句柄
all_h = driver.window_handles

# 这里打印出来的所有页面句柄是一个[]list
print all_h  # 打印所有的句柄

# 方法一：判断句柄，不等于首页就切换
# for i in all_h:
#     if i != h:
#         driver.switch_to.window(i)
#         print driver.title

# 方法二：获取list里面第二个直接切换
driver.switch_to.window(all_h[1])
print driver.title

# 关闭新窗口
# driver.close()

# 切换到首页句柄
driver.switch_to_window(h)
time.sleep(2)

driver.close()
# 打印当前的title
print driver.title