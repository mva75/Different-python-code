#Программа рисует квадратную спираль
#Надо открыть еще какой нибудь графический редактор(Paint) и после запуска программы переместить мышку туда
import pyautogui, time

time.sleep(5)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)



