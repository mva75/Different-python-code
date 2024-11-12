# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
#keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://mva75.github.io/Gallery-CSS/pages/gradient/gradient_example2.html")

# get element 
#element = driver.find_element(By.XPATH ,"//a[@title='Telegram']") Save example XPATH
element = driver.find_element(By.CSS_SELECTOR, 'nav.navbar')

# print complete element
print(element)

#driver.quit()
