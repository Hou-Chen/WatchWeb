from django.shortcuts import render
import datetime

def main(request):
    now = datetime.datetime.now()
    context = {'link':'Django很棒', 'now':now}
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')