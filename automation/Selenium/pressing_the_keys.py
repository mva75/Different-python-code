# Реализовано нажатие клавиш(END, HOME)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://nostarch.com')

htmlElem = driver.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)


