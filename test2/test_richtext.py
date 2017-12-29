# _*_ coding: UTF-8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 配置文件地址
profile_directory = r'C:\Users\123\AppData\Roaming\Mozilla\Firefox\Profiles\cr0ic2ar.default'
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
# 打开博客园地址
bolgurl = "https://www.cnblogs.com/"
# 定义打开自己的博客园
cyfbolg = bolgurl + "cyfyywfc"
driver.get(cyfbolg)
# 定位点击新随笔按钮
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(3)
# 定义标题输入内容
eaittile = u"test学习方向"
# 定义主题输入内容
eaitbody = u"学习经典的测试理论和软件工程知识。（长期学习） 学习一门编程语言，" \
           u"按顺序推荐python, java(贪多嚼不烂，如果是非常资深的测试开发已经会了前两种，" \
           u"还可以学习javascript） 掌握黑盒自动化测试技术，推荐学习selenium, appium " \
           u"掌握接口功能测试技术， 推荐学习python+requests或者java+httpclient 掌握1个或者多个自动测试框架，" \
           u"推荐学习robotframework, python的unittest, java的TestNG, 了解Java的Cucumber 掌握性能测试技术，" \
           u" 推荐学习jmeter, loadrunner 学习与人相处，团队协作，带领团队。"
# 定位标题部分引用eaittile
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(eaittile)
# 切换iframe
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
# 定位输入富文本tab缩进
driver.find_element_by_id("tinymce").send_keys(Keys.TAB)
driver.find_element_by_id("tinymce").send_keys(eaitbody)
time.sleep(3)
# 释放iframe，重新回到主界面上
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_id("Editor_Edit_lkbPost").click()

driver.close()