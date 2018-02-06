# _*_ coding: UTF-8 _*_
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# css通过id属性定位
# driver.find_element_by_css_selector("#kw").send_keys("python")

# css通过class属性定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("python")

# css通过标签来属性定位
# driver.find_element_by_css_selector("input").send_keys("python")

# css通过name属性定位
# driver.find_element_by_css_selector("[name='wd']").send_keys("python")

# css通过autocomplete属性定位.
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("小白兔去哪了")

# css通过type属性定位
# driver.find_element_by_css_selector("[type='text']").send_keys("小白兔去哪了")

# driver.find_element_by_css_selector("input:contains('kw')")

# css通过标签与class属性组合定位
# driver.find_element_by_css_selector("[input.s_put]").send_keys("小白兔去哪了")

# css通过标签与id属性组合定位
# driver.find_element_by_css_selector("[input#kw]").send_keys("小白兔去哪了")

# css通过标签与其他属性组合定位
driver.find_element_by_css_selector("[input[id='kw']").send_keys("小白兔去哪了")

time.sleep(2)


driver.quit()