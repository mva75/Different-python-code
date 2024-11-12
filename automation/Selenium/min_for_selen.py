#В этом коде самый минимум по selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Обозначаем драйвер для браузера
driver = webdriver.Firefox()

#Заходим на сайт
driver.get("https://mva75.github.io/Gallery-CSS/pages/gradient/gradient.html")

#Находим элемент(в данном случае по ID)
mva = driver.find_element(By.ID, 'home')

#Кликаем по элементу
mva.click()
