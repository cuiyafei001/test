# _*_ coding: UTF-8 _*_
from selenium import webdriver

# 加载Chrome配置
option = webdriver.ChromeOptions()

# 伪装iphone登录
# option.add_argument('--user-agent=iphone')

# 伪装android
option.add_argument('--user-agent=android')
driver = webdriver.Chrome(chrome_options=option)

driver.get("htpp://www.taobao.com/")
