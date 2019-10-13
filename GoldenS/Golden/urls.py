from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prodone/', views.prodone, name='prodone'),
    path('prodtwo/', views.prodtwo, name='prodtwo'),
    path('prodthree/', views.prodthree, name='prodtwo'),
    path('track/', views.track, name='track'),
    path('send/', views.quicksend, name='send'),
]