# Эта программа выводит введенный адрес в google.maps
import webbrowser

place = input('Введите адрес ') # Город, улица
adress = ('http://google.com/maps/place/')+ place

webbrowser.open(adress)


