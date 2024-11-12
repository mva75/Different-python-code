# Эта программа загружает файл RomeoAndJuliet.txt
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') # Вызов функции requests.get() для загрузки файла
res.raise_for_status() # Проверка

playFile = open('RomeoAndJuliet.txt', 'wb') # Вызов функции open() с аргументом 'wb' для создания нового файла
for chunk in res.iter_content(100000): # Цикл метода iter_content() объекта Response
    playFile.write(chunk) # Вызов метода write() на каждой итерации для записи файла
    

playFile.close() # Закрытие   
    






