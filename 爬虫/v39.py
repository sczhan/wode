import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 可能需要手动添加路径
# path = r"C:\Users\111\Desktop\chromedriver.exe"
# drivers = webdriver.Chrome(path)
drivers = webdriver.Chrome()

url = "http://www.baidu.com"

drivers.get(url)

text = drivers.find_element_by_id("wrapper").text
print(text)
print(drivers.title)

# 得到页面的快照
drivers.save_screenshot("index.png")

# id="kw"的是百度的输入框,我们得到输入框的UI元素后直接输入大熊猫
drivers.find_element_by_id("kw").send_keys(u"大熊猫")

# id="su"是百度搜索的按钮, click模拟点击
drivers.find_element_by_id("su").click()

time.sleep(5)
drivers.save_screenshot("大熊猫.png")

# 获取当前页面的cookie
print(drivers.get_cookies())

# 模拟输入两个按键 ctrl+a
drivers.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
# ctrl+x 是剪切快捷键
drivers.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

drivers.find_element_by_id("kw").send_keys(u"航空母舰")
drivers.save_screenshot("航空母舰.png")

drivers.find_element_by_id("su").send_keys(Keys.RETURN)
time.sleep(5)

drivers.save_screenshot("航母2.png")

# 清空输入框, clear
drivers.find_element_by_id("kw").clear()
drivers.save_screenshot("清空.png")

# 关闭浏览器
drivers.quit()