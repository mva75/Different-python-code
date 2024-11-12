#Реализовано заполнение и отправка формы на примере Email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://gmail.com')

emailElem = driver.find_element(By.ID, 'identifierId')
emailElem.send_keys('qwert@gmail.com')
emailElem.send_keys(Keys.RETURN)
#emailElem = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b').click()

driver.quit()

 
