# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "file:///C:/Users/123/Desktop/table.HTML"
driver.get(url)

t = driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[2]/td[3]")
print t.text

driver.quit()


