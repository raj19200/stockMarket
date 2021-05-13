from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.sendemail, name="stockSendemail"),
    path('', views.index, name="stockHome"),
    path('contact', views.contact, name="stockContact"),
    path('about', views.about, name="stockContact"),
    
]