"""
任务:
1. 通过selenium 模拟对月面元素的控制

"""

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 通过js控制页面内容
# 需要先把js编写出来
# 然后通过execute_script执行

# 美化输入框, 输入框id是kw
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"

# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot("redbaidu.png")

# js隐藏相应元素, 我们这里隐藏logo
img = driver.find_element_by_xpath("//*[@id='lg']/img")
driver.execute_script("$(arguments[0]).fadeOut()", img)

# 滚定滑动条到最底下
js = "$('.scroll_top').click( function(){$('html, body').animate({scrollTop: '0px'}, 1500)});"

# 查看网页快照
time.sleep(3)
driver.save_screenshot("nullbaidu.png")
driver.quit()