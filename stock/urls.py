from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.sendemail, name="stockSendemail"),
    path('', views.index, name="stockHome"),
    path('contact', views.contact, name="stockContact"),
    path('about', views.about, name="stockContact"),
    path('services',views.services, name="stockservices"),
    path('intraday',views.intraday, name="intraday"),
    path('shortterm',views.shortterm, name="shortterm"),
    path('mediumterm',views.mediumterm, name="mediumterm"),
    path('longterm',views.longterm, name="longterm"),
    path('formcheck',views.formcheck,name="formcheck"),
    path('formpage',views.formpage,name="formpage"),
]