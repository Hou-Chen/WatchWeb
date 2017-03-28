import smtplib
fromaddr = 'houchen691@gmail.com'
toaddrs  = 'a40208s@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


username = 'a40208s@gmail.com'
password = 'a941103s'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()