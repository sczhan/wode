
"""
豆瓣电影
"""
from selenium import webdriver


driver = webdriver.PhantomJS()

driver.get("https://movie.douban.com/")

# 第一次截图
driver.save_screenshot("豆瓣1.png")

# 向下滚动10000像素
js = "document.body.scrollTop=10000"
js = "var q=document.documentElement.scrollTop=10000"

driver.execute_script(js)
driver.implicitly_wait(2)

driver.save_screenshot("豆瓣2.png")

driver.quit()