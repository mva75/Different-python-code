"""
Восемь основных компонентов
1. Начните сеанс
2. Выполните действия в браузере
3. Запрос информации о браузере
4. Разработайте стратегию ожидания
5. Найдите элемент
6. Примите меры по отношению к элементу
7. Запрос информации об элементе
8. Завершите сеанс
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(1)

#Если ищем два и более элементов одного значения, то используем driver.find_elements
text_box = driver.find_element(By.NAME, value="my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(By.ID, value="message")
text = message.text

driver.quit()
  
