
from selenium import webdriver


driver = webdriver.PhantomJS()
url = "https://www.jianshu.com/p/f5c5ede490be"

driver.get(url)

driver.implicitly_wait(5)

print(driver.page_source)
author = driver.find_element_by_xpath("//span[@class='_22gUMi']").text

# data = driver.find_element_by_xpath("//span[@class='_3tCVn5']/time").text
#
# word = driver.find_element_by_xpath("//span[@class='_3tCVn5']/span").text.strip()
"wordage"
print(author, 1)