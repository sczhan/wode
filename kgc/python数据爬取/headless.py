from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='F:\wode\kgc\python数据爬取\chromedriver.exe', chrome_options=options)
driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.510a5e0a9eMaBx&id=614310192380&skuId=4332977805337&user_id=1921849732&cat_id=2&is_b=1&rn=fca20f9bbb1c2cbff748292b2a8d9ded")
# action_chain = action_chains.ActionChains(driver)
# a = driver.find_element_by_id("sufei-dialog-close")
#
# action_chain.click(a).perform()
# time.sleep(10)
print(driver.page_source)
# elements = driver.find_elements_by_class_name("txt")
# print(elements)
# for element in elements:
#     print(element.text)
# elements = driver.find_elements_by_xpath('//nav[@class="nav area"]')
# print(elements)
# for element in elements:
#     print(element.text)
# driver.close()
# driver.quit()
# elements = driver.find_elements_by_tag_name("a")
# print(elements)
# for element in elements:
#     print(element.text)
driver.close()
driver.quit()