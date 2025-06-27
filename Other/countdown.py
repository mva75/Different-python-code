#Программа обратного отчета времени и открытия файлов и сайтов по прошествии этого времени

import time, subprocess, webbrowser

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft -1

subprocess.Popen(['start', 'alone.mp3'], shell=True) 
subprocess.Popen(['start', 'combi.pdf'], shell=True)
webbrowser.open('https://nv86.ru/')