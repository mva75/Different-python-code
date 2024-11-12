# Показывается переход по ссылке
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://inventwithpython.com')

# Сделаем скриншот всей страницы
driver.get_full_page_screenshot_as_file('foo.png')

linkElem = driver.find_element(By.LINK_TEXT, 'Read Online for Free')
type(linkElem)
linkElem.click() # перейти по ссылке "Read Online for Free"

# А здесь сделаем скриншот только видимой части страницы
driver.save_screenshot('screenshot.png')
