# import the libs
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://inventwithpython.com')

try:
    elem = driver.find_element(By.CLASS_NAME, 'navbar-brand')
    print('Найден элемент <%s> с данным именем класса!' %(elem.tag_name))
except:
    print('Не удалось найти элемент с данным именем класса')
