# _*_ coding: UTF-8 _*_
from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/cyfyywfc/")

# 使用selenium提供的page_source方法获取页面源码
page = driver.page_source
# print page
# "非贪婪匹配，re.S(','匹配字符，包括换行符)"
url_list = re.findall('href=\"(.*?)\"',page,re.S)
url_all = []
for url in url_list:
    if 'http' in url:
        print url
        url_all.append(url)
# 最终的URL集合
print url_all

driver.quit()
