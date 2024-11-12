# Это незавершенный проект по скачиванию фотографии с сайта. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://Imgur.com')

driver.implicitly_wait(1)
fotoElem = driver.find_element(By.CLASS_NAME, 'Searchbar-textInput')
fotoElem.send_keys('cars')
fotoElem.send_keys(Keys.RETURN)
imgElem = driver.find_element(By.CLASS_NAME, 'post')
#action.context_click(on_element = element)
#imgElem.context_click()
imgElem.click()
rightElem = driver.find_element(By.CLASS_NAME, 'image-placeholder')
#rightElem.context_click()
