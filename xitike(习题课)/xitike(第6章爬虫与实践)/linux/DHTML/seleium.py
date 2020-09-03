
"""
动态 html

JS(JavaScript)   一般嵌入在多媒体文件中, 网页游戏

JQuery    在源代码中包含JQuery入口
            <script type="text/javascript" src= "httpd://......../jquery-1.11.1.min.js?v=34234></script>

Ajax

DHTML  类似于Ajax  (Dynamic HTML)

如何结局这类页面的数据抓取
    1. 直接从js中采集内容 (费事费力)
    2. 利用python的第三方库直接运行js
    3. selenium && PhantomJS

selenium
    是一个web的自动化测试工具
    可以指定命令自动操作
    让浏览器自动加载数据, 截屏, 判断网站上某些动作是否发生

    安装
        pip install selenium==2.48.0
        https://pypi.org/simple/selenium/

    参考文档
        http://selenium-python.readthedocs.io/index.html

PhantomJs
    基于Webkit的无界面浏览器
    selenium + PhantomJs

    安装:
        http://phantomjs.org/download.html
        将安装路径添加到环境变量
"""

import time

# 导入webdriver
from selenium import webdriver
# 若想调用键盘按键需要引入keys包
from selenium.webdriver.common.keys import Keys

# 创建浏览器对象 executable_path=指定PhantomJS路径
driver = webdriver.PhantomJS()


# get方法
driver.get("http://www.baidu.com")

# 生成当前页面快照并保存
# driver.save_screenshot("baidu.png")
# print(driver.title)

# 模拟百度搜索
# id="kw"  输入美女,并点击
driver.find_element_by_id("kw").send_keys(u"美女")

# id=su
driver.find_element_by_id("su").click()
time.sleep(2)

driver.save_screenshot("girl.png")

# 打印当前页面源码
# print(driver.page_source)

# 获取当前页面cookie信息
# print(driver.get_cookies())

# 发送ctrl + x 剪切输入框中的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

driver.save_screenshot("girl2.png")

# 清空
driver.find_element_by_id("kw").clear()

# 再次输入内容
driver.find_element_by_id("kw").send_keys(u"大熊猫")
driver.find_element_by_id("su").click()
time.sleep(10)
driver.save_screenshot("3.png")

# 打印当前url地址
print(driver.current_url)
driver.quit()


"""
定位元素:
    find_element_by_id
"""
