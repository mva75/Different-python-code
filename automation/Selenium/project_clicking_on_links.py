# Программа перехода по ссылкам
# Доработать открытие последней ссылки(чтобы открывалась главная новость)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://nv86.ru/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Работа").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Афиша").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Карта").click()
#driver.find_element(By.CLASS_NAME, "news-item__link mr-1").click()






