"""
模拟豆瓣登录
url = "https://www.douban.com/"

"""
from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("https://www.douban.com/")
driver.implicitly_wait(5)
print(driver.page_source)

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("13222057990")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("wang1998")
driver.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()
driver.implicitly_wait(1)

with open("douban.html", "w", encoding="utf-8")as f:
    f.write(driver.page_source)

print(driver.current_url)

