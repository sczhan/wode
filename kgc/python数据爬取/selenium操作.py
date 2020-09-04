import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome('F:\wode\kgc\python数据爬取\chromedriver.exe')
# driver.get("http://sahitest.com/demo/clicks.htm")
#
# click_btn = driver.find_element_by_xpath('//input[@value="click me"]')  # 单击按钮
# doubleclick_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')  # 双击按钮
# rightclick_btn = driver.find_element_by_xpath('//input[@value="right click me"]')  # 右击按钮
#
# actionChinas = action_chains.ActionChains(driver)
# actionChinas.click(click_btn).double_click(doubleclick_btn).context_click(rightclick_btn).perform()
# time.sleep(10)
# a = driver.find_element_by_xpath("//textarea").get_attribute("value")
# print(a, 1)
# driver.close()
# driver.quit()

driver = webdriver.Chrome('F:\wode\kgc\python数据爬取\chromedriver.exe')
driver.get("http://sahitest.com/demo/selectTest.htm")
element = driver.find_element_by_id("s1")
select = Select(element)
select.select_by_index(2)
time.sleep(10)
select.select_by_value("51")
time.sleep(10)
select.select_by_visible_text("Fax")
time.sleep(10)

print(select.all_selected_options)
print(select.first_selected_option)
driver.close()
driver.quit()
