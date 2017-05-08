from django.shortcuts import render
from main import send

def main(request):
    return render(request, 'main/main.html')
def related(request):
    return render(request, 'main/related.html')
def service(request):
    return render(request, 'main/service.html')
def tool(request):
    return render(request, 'main/tool.html')
def ARMANI(request):
    return render(request, 'main/ARMANI/ARMANI.html')
def SEIKO(request):
    return render(request, 'main/SEIKO/SEIKO.html')
def IWC(request):
    return render(request, 'main/IWC/IWC.html')
def CITIZEN(request):
    return render(request, 'main/CITIZEN/CITIZEN.html')
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
def OTHER(request):
    return render(request, 'main/OTHER/OTHER.html')
def OTHER_0321(request):
    return render(request, 'main/OTHER/OTHER_0321.html')
def email(request):    
    return render(request, 'main/email.html', send.send(request))