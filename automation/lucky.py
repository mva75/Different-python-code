# Программа для открытия нескольких результатов поиска с помощью Google
# Надо доработать, браузер не открывается
import requests, sys, webbrowser, bs4

print('Гуглим...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, features="html.parser")
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
