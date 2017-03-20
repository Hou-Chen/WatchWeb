from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

def main(request):
    return render(request, 'main/main.html')
def ARMANI(request):
    return render(request, 'main/ARMANI.html')
def SEIKO(request):
    return render(request, 'main/SEIKO.html')
def CHOPARD(request):
    return render(request, 'main/CHOPARD.html')
def IWC(request):
    return render(request, 'main/IWC.html')
def CITIZEN(request):
    return render(request, 'main/CITIZEN.html')
def HAMILTON(request):
    return render(request, 'main/HAMILTON.html')
def MIDO(request):
    return render(request, 'main/MIDO.html')
def TAGHeuer(request):
    return render(request, 'main/TAGHeuer.html')
def Omega(request):
    return render(request, 'main/Omega.html')
def LONGINES(request):
    return render(request, 'main/LONGINES.html')
def Fossil(request):
    return render(request, 'main/Fossil.html')
def DanielWellington(request):
    return render(request, 'main/DanielWellington.html')
def ROLEX(request):
    return render(request, 'main/ROLEX.html')
def ORIS(request):
    return render(request, 'main/ORIS.html')                         
def PANERAI(request):
    return render(request, 'main/PANERAI.html')
def TISSOT(request):
    return render(request, 'main/TISSOT.html')


class EmailForm(forms.Form):
    Email = forms.EmailField()


def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            new_email = form.save()
            return HttpResponseRedirect('/email/' + str(new_email.pk))
        
    form = EmailForm()
    return render(request, 'main/email.html', {'form' : form})
