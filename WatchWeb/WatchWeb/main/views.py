from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
import time

def main(request):
    return render(request, 'main/main.html')
def ARMANI(request):
    return render(request, 'main/ARMANI/ARMANI.html')
def SEIKO(request):
    return render(request, 'main/SEIKO/SEIKO.html')
def CHOPARD(request):
    return render(request, 'main/CHOPARD/CHOPARD.html')
def IWC(request):
    return render(request, 'main/IWC/IWC.html')
def IWC_0321(request):
    return render(request, 'main/IWC/IWC_0321.html')
def CITIZEN(request):
    return render(request, 'main/CITIZEN/CITIZEN.html')
def HAMILTON(request):
    return render(request, 'main/HAMILTON/HAMILTON.html')
def MIDO(request):
    return render(request, 'main/MIDO/MIDO.html')
def TAGHeuer(request):
    return render(request, 'main/TAGHeuer/TAGHeuer.html')
def Omega(request):
    return render(request, 'main/Omega/Omega.html')
def LONGINES(request):
    return render(request, 'main/LONGINES/LONGINES.html')
def Fossil(request):
    return render(request, 'main/Fossil/Fossil.html')
def DanielWellington(request):
    return render(request, 'main/DanielWellington/DanielWellington.html')
def ROLEX(request):
    return render(request, 'main/ROLEX/ROLEX.html')
def ORIS(request):
    return render(request, 'main/ORIS/ORIS.html')                         
def PANERAI(request):
    return render(request, 'main/PANERAI/PANERAI.html')
def TISSOT(request):
   return render(request, 'main/TISSOT/TISSOT.html')

class Success(tk.Frame):
    def __init__(self,master):
        self.master=master
        tk.Frame.__init__(self,master)
        self.pack()
        self.createwidget()
    def createwidget(self):
        self.label = tk.Label(self,text='寄送成功')
        self.label.pack()
        self.button = tk.Button(self,text="確定",command=self.closeme)
        self.button.pack()
    def closeme(self):
        self.master.destroy()
        self.master.quit()
class Miss(tk.Frame):
    def __init__(self,master):
        self.master=master
        tk.Frame.__init__(self,master)
        self.pack()
        self.createwidget()
    def createwidget(self):
        self.label = tk.Label(self,text='寄送失敗')
        self.label.pack()
        self.button = tk.Button(self,text="確定",command=self.closeme)
        self.button.pack()
    def closeme(self):
        self.master.destroy()
        self.master.quit()     
class No(tk.Frame):
    def __init__(self,master):
        self.master=master
        tk.Frame.__init__(self,master)
        self.pack()
        self.createwidget()
    def createwidget(self):
        self.label = tk.Label(self,text='未填滿')
        self.label.pack()
        self.button = tk.Button(self,text="確定",command=self.closeme)
        self.button.pack()
    def closeme(self):
        self.master.destroy()
        self.master.quit()
        
def email(request):
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
            if request.POST['submit'] == '送出':                  
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(fromaddr,password)
                try:
                    click = False
                    global click          
                    server.sendmail(fromaddr, toaddrs, msg.as_string())                 
                    server.quit()
                    time.sleep(1)
                    click=True
                    if click == True:
                        root = tk.Tk()
                        app = Success(master=root)
                        #app.createwidget(0)
                        root.mainloop()
                except:            
                        root = tk.Tk()
                        app = Miss(master=root)
                        #app = Success(master=root)
                        #app.createwidget(1)
                        root.mainloop()
        else:
            root = tk.Tk()
            app = No(master=root)
            #app = Success(master=root)
            #app.createwidget(2)
            root.mainloop()
    return render(request, 'main/email.html')

#class Success(tk.Frame):
#    def __init__(self,master):
#        self.master=master
#        tk.Frame.__init__(self,master)
#        self.pack()
#        data = {0:'su', 1:'mi', 2:'no'}
#        self.createwidget(data)
#    def createwidget(self, data):
#        if data == 'su':
#            self.label = tk.Label(self,text='寄送成功')
#            self.label.pack()
#            self.button = tk.Button(self,text="確定",command=self.closeme)
#            self.button.pack()
#        elif data == 'mi':
#            self.label = tk.Label(self,text='寄送失敗')
#            self.label.pack()
#            self.button = tk.Button(self,text="確定",command=self.closeme)
#            self.button.pack()
#        elif data == 'no':
#            self.label = tk.Label(self,text='未填滿')
#            self.label.pack()
#            self.button = tk.Button(self,text="確定",command=self.closeme)
#            self.button.pack()
#    def closeme(self):
#        self.master.destroy()