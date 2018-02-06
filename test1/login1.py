# _*_ coding: UTF-8 _*_
# 函数登录的账号和密码参数化
from selenium import webdriver
import time
def login(user,password):
    driver.get("http://testerhorde.com/")
    driver.find_element_by_xpath(".//*[@id='ember808']/header/div/div/div[2]/span/button[2]").click()
    driver.find_element_by_xpath(".//*[@id='login-account-name']").send_keys(user)
    driver.find_element_by_xpath(".//*[@id='login-account-password']").send_keys(password)
    driver.find_element_by_css_selector(".btn.btn-large.btn-primary").click()
    return driver
def logout():
    driver.find_element_by_xpath(".//*[@id='current-user']/a/div/img").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='ember808']/header/div/div/div[2]/div/div/div/div/div[3]/ul/li/a").click()
    time.time(1)
    driver.quit()
#   运行用例
#   1.先调用登录函数
#   2.检查登录结果
#   3.退出登录，并关闭浏览器
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver = login("csliyi001","123456789")
    t = driver.find_element_by_xpath(".//*[@id='current-user']/a/div/img").get_attribute("title")
    if  t == "csliyi001":
        print("登陆成功")
    else:
        print("登录失败")

    logout()