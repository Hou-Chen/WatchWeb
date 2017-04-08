import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *

def send(request):
    if request.method == 'POST':
        fromaddr = 'a40208s@gmail.com'
        password = 'a941103s'
        toaddrs = 'houchen691@gmail.com'        
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = 'WatchWeb'
        if request.POST['name'] and request.POST['email'] and request.POST['message'] != '':
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']                       
            body = name + "\n\n" + email + "\n\n" + message
            msg.attach(MIMEText(body, 'plain'))              
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(fromaddr,password)
            try:
                server.sendmail(fromaddr, toaddrs, msg.as_string())
                server.quit()
                su('su')
            except:            
                su('mi')
        else:
            su('no')

class Success(Frame):
    def __init__(self,master):
        self.master=master
        Frame.__init__(self,master, bg="white")
        self.pack()
        data = ('su','mi','no')
        self.createwidget(data)
    def createwidget(self, data):        
        if data == 'su':
            self.label = Label(self,text='寄送成功', font=1, width=30, height=3, bg="white")
            self.label.pack()
            self.button = Button(text="確定",command=self.closeme, font=1, width=10)
            self.button.pack()
        elif data == 'mi':
            self.label = Label(self,text='寄送失敗', font=1, width=30, height=3, bg="white")
            self.label.pack()
            self.button = Button(self,text="確定",command=self.closeme, font=1, width=10)
            self.button.pack()
        elif data == 'no':
            self.label = Label(self,text='未填滿', font=1, width=30, height=3, bg="white")
            self.label.pack()
            self.button = Button(self,text="確定", command=self.closeme,font=1, width=10)
            self.button.pack()
    def closeme(self):
        self.master.destroy()
def su(data):
    root = Tk()
    root.title("Message")
    root.resizable(width=False, height=False)
    root.configure(background="white")
    app = Success(master=root)
    app.createwidget(data)
    root.mainloop()