
"""
利用selenium执行js脚本

"""

from selenium import webdriver


driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com")


#让输入有红颜色框脚本
js = 'var j=document.getElementById("kw");j.style.border="2px solid red"'

# 调用搜索输入框的脚本
driver.execute_script(js)

# 快照截图
driver.implicitly_wait(2)
# driver.save_screenshot("red_baidu.png")

# # 使用js隐藏图片
# img = driver.find_element_by_xpath("//*[@id='lg']/img")
#
# driver.execute_script("$(arguments[0]).fadeOut()", img)
#
# driver.save_screenshot("no_baidu.png")

# 向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html, body').animate({scrollTop: '0px'}, 800);})")

driver.implicitly_wait(2)
driver.save_screenshot("null_baidu.png")