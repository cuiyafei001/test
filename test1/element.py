# _*_ coding: UTF-8 _*_
# 第一步打入webdriver模块
from selenium import webdriver
import time
# 第二步打开浏览器
driver = webdriver.Firefox()
# 第三步打开百度
driver.get("https://www.baidu.com/")
# 设置休眠时间为3秒，也可以是小数，单位是秒
time.sleep(3)
# 等待三秒后刷新页面
driver.refresh()
# driver.get("http://www.ctrip.com/")
# time.sleep(5)
# 返回上一页
# driver.back()
# time.sleep(3)
# 切换到下一页
# driver.forward()
# driver.set_window_size(540,960)
# time.sleep(2)
# 将浏览器窗口最大化
driver.maximize_window()
#对屏幕进行截屏
driver.get_screenshot_as_file("E:\\test\\b1.jpg")
driver.close() # 关闭当前窗口
# quit用于退出浏览器进程
# driver.quit()
# 通过id定位百度搜索框，并输入“python”
# driver.find_element_by_id("kw").send_keys("python")
# 通过name定位百度搜索框，并输入“python”
# driver.find_element_by_name("wd").send_keys("python")
# 通过class定位百度搜索框，并输入“python”
# driver.find_element_by_class_name("s_ipt").send_keys("python")
# 通过tag(标签)定位百度搜索框，并输入“python”
# driver.find_element_by_tag_name("input ").send_keys("python")
# 通过link（超链接）属性点位到hao123按钮，并点击
# driver.find_element_by_link_text("hao123").click()
# driver.find_element_by_partial_link_text("ao123").click()
# 返回上一页
# driver.back()
# time.sleep(3)
# 切换到下一页
# driver.forward().
# 在FirePath里copy出xpath地址
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
# 用xpath通过id属性定位
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
# 用xpath通过name属性定位
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")
# 用xpath通过class属性定位
# driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("python")
# 用xpath其他属性定位
# driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("python")
# driver.quit()
# time.sleep(3)
# driver.quit()