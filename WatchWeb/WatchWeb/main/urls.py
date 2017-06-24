from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^email/', views.email, name='email'),
    url(r'^ARMANI/', views.ARMANI, name='ARMANI'),
    url(r'^SEIKO/', views.SEIKO, name='SEIKO'),
    url(r'^OTHER/', views.OTHER, name='OTHER'),
    url(r'^OTHER_0321/', views.OTHER_0321, name='OTHER_0321'),
    url(r'^IWC/', views.IWC, name='IWC'),    
    url(r'^CITIZEN/', views.CITIZEN, name='CITIZEN'),
    url(r'^MIDO/', views.MIDO, name='MIDO'),
    url(r'^TAGHeuer/', views.TAGHeuer, name='TAGHeuer'),
    url(r'^Omega/', views.Omega, name='Omega'),
    url(r'^Omega_0509/', views.Omega_0509, name='Omega_0509'),
    url(r'^LONGINES/', views.LONGINES, name='LONGINES'),
    url(r'^Fossil/', views.Fossil, name='Fossil'),
    url(r'^DanielWellington/', views.DanielWellington, name='DanielWellington'),
    url(r'^ROLEX/', views.ROLEX, name='ROLEX'),
    url(r'^ROLEX_0519/', views.ROLEX_0519, name='ROLEX_0519'),
    url(r'^ROLEX_0520/', views.ROLEX_0520, name='ROLEX_0520'),
    url(r'^ORIS/', views.ORIS, name='ORIS'),
    url(r'^PANERAI/', views.PANERAI, name='PANERAI'),
    url(r'^TISSOT/', views.TISSOT, name='TISSOT'),
]