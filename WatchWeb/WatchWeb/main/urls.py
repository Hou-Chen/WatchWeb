from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^email/', views.email, name='email'),
    url(r'^ARMANI/', views.ARMANI, name='ARMANI'),
    url(r'^SEIKO/', views.SEIKO, name='SEIKO'),
    url(r'^CHOPARD/', views.CHOPARD, name='CHOPARD'),
    url(r'^IWC/', views.IWC, name='IWC'),
    url(r'^IWC_0321/', views.IWC_0321, name='IWC_0321'),
    url(r'^CITIZEN/', views.CITIZEN, name='CITIZEN'),
    url(r'^HAMILTON/', views.HAMILTON, name='HAMILTON'),
    url(r'^MIDO/', views.MIDO, name='MIDO'),
    url(r'^TAGHeuer/', views.TAGHeuer, name='TAGHeuer'),
    url(r'^Omega/', views.Omega, name='Omega'),
    url(r'^LONGINES/', views.LONGINES, name='LONGINES'),
    url(r'^Fossil/', views.Fossil, name='Fossil'),
    url(r'^DanielWellington/', views.DanielWellington, name='DanielWellington'),
    url(r'^ROLEX/', views.ROLEX, name='ROLEX'),
    url(r'^ORIS/', views.ORIS, name='ORIS'),
    url(r'^PANERAI/', views.PANERAI, name='PANERAI'),
    url(r'^TISSOT/', views.TISSOT, name='TISSOT'),
]