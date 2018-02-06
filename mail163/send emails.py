# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

# 配置文件地址
profile_directory = r'C:\Users\123\AppData\Roaming\Mozilla\Firefox\Profiles\cr0ic2ar.default'

# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)

# 启动浏览器配置
driver = webdriver.Firefox(profile)
url = 'http://mail.163.com/'
driver.get(url)
time.sleep(2)

driver.switch_to.frame("x-URS-iframe")
time.sleep(2)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("cuiyafei001")
driver.find_element_by_name("password").send_keys("110120119.com/.,")
driver.find_element_by_id("dologin").click()
# 释放iframe
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='_mail_component_70_70']/span[2]").click()
time.sleep(2)

driver.find_element_by_class_name("nui-editableAddr-ipt").clear()
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("990965612@qq.com")
# 定位邮件的主题并输入信息
# driver.find_elements_by_xpath(".//*[@id='1514276026803_subjectInput']").clear()
driver.find_elements_by_class_name("nui-ipt-input")[2].send_keys(u"你加班吗")
driver.find_element_by_xpath('//input[@type="file"]').send_keys("F:\souga.png")

iframe = driver.find_element_by_class_name("APP-editor-iframe")  #若iframe有id或是name属性，可以直接切换
driver.switch_to.frame(iframe)


driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys(u"几点走")

driver.switch_to_default_content()

driver.find_element_by_id("_mail_icon_43_226").click()
time.sleep(3)

driver.close()
