# Программа загрузки избранного
# В данном случае ссылки на документацию по скрапингу
import webbrowser

favourites = input('Введите избранное ')

scrapy = ('https://scrapy.org/')
selenium = ('https://www.selenium.dev/')
beautiful_soup = ('http://bs4ru.geekwriter.ru/bs4ru.html?ysclid=m39u81wnff133639285')
requests = ('https://requests.readthedocs.io/en/latest/user/quickstart/')
omegaT = ('https://omegat.org/ru/')

if favourites == '1':
    webbrowser.open(scrapy)
elif favourites == '2':
    webbrowser.open(selenium)
elif favourites == '3':
    webbrowser.open(beautiful_soup)
elif favourites == '4':
    webbrowser.open(requests)
else:
    webbrowser.open(omegaT) # А иначе загружаем программу для переводов документации
    
