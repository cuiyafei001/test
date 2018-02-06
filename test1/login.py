# _*_ coding: UTF-8 _*_
# 登录社区
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://hordehome.com/")
# 设置隐试等待10秒
driver.implicitly_wait(10)
driver.maximize_window()
# 点击登录按钮，输入账号密码后登录
driver.find_element_by_xpath(".//*[@id='ember808']/header/div/div/div[2]/span/button[2]").click()
driver.find_element_by_id("login-account-name").send_keys("csliyi001")
driver.find_element_by_id("login-account-password").send_keys("123456789")
driver.find_element_by_css_selector(".btn.btn-large.btn-primary").click()
time.sleep(5)
# 1.登录完成之后，需要检查是否登录成功，这里就需要有个检查点，我这边选择的是查看登录后头像的属性
# 2.先定位到登录头像，通过get_attribute()方法获取到这个对象的title属性
# 3.判断获取到的值，与期望结果是否一致
# 4.符合预期结果测试通过
# 5.不符合预期结果测试不通过
# 获取头像的title属性值
time.sleep(3)
t = driver.find_element_by_xpath(".//*[@id='current-user']/a/div/img").get_attribute("title")
time.sleep(2)
# 判断返回结果
if t == "csliyi001":
    print("登陆成功")
else:
    print("登录失败")
# 1.测试完之后，别忘了最后退出登录
# 2.退出登录后，关闭浏览器
# 退出登录
driver.find_element_by_id("current-user").click()
driver.find_element_by_id("ember808").click()
driver.quit()