# _*_ coding: UTF-8 _*_
from selenium import webdriver

# 配置文件地址
profile_directory = r'C:\Users\123\AppData\Roaming\Mozilla\Firefox\Profiles\cr0ic2ar.default'

# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)

# 启动浏览器配置
driver = webdriver.Firefox(profile)
url = "https://www.baidu.com/"
driver.get(url)
