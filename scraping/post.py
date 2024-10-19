import smtplib 
from email.mime.text import MIMEText   
msg = MIMEText('The body of the email is here')   
msg['Subject'] = 'An Email Alert' 
msg['From'] = 'nik-lentyaj@yandex.ru'
msg['To'] = 'slava75144@gmail.com'
s = smtplib.SMTP('localhost') 
s.send_message(msg) 
s.quit()