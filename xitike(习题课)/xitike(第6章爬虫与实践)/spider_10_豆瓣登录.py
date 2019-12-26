
"""
利用selenium,模拟登录豆瓣
需要验证码
思路:
1. 保存页面生成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作
url: https:accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001
"""
import time

from selenium import webdriver

url = "https:accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)

# 生成快照,用老查看验证码
driver.save_screenshot("豆瓣_index.png")
captcha = input("plz input your codes:")

# 利用账号信息和验证码登录
driver.find_element_by_id("e").send_keys("1322")
driver.find_element_by_id("").send_keys("")
driver.find_element_by_id("").send_keys(captcha)

driver.find_element_by_xpath("//input[@]").click()
time.sleep(5)

driver.save_screenshot("logined.png")

with open("doubandenglu.html", "w", encoding="utf-8")as f:
    f.write(driver.page_source)
driver.quit()


