
"""
通过WebDriver操作百度进行查找
"""
from selenium import webdriver

# 通过Keys模拟键盘


# 操作那个浏览器就对那个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
driver = webdriver.PhantomJS()

# 如果浏览器没有在相应环境变量中, 需要指定浏览器位置
driver.get("http://www.baidu.com")

# 通过函数查找title标签
print("Title: {0}".format(driver.title))