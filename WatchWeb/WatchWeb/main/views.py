from django.shortcuts import render
import smtplib

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
def email(request):
    fromaddr = 'a40208s@gmail.com'
    toaddrs  = 'houchen691@gmail.com'
    msg = 'Test'
    
    username = 'a40208s@gmail.com'
    password = 'a941103s'
        
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()    
    return render(request, 'main/email.html')
    


