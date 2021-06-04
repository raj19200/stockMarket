from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInformation,Form

# import pyrebase
# config = {
#     "apiKey": "AIzaSyBcQRbf3ECXHAUAe9JpPul976Wg3HyikbE",
#     "authDomain": "contactform-e91b3.firebaseapp.com",
#     "databaseURL": "https://contactform-e91b3-default-rtdb.firebaseio.com",
#     "projectId": "contactform-e91b3",
#     "storageBucket": "contactform-e91b3.appspot.com",
#     "messagingSenderId": "416109208283",
#     "appId": "1:416109208283:web:fe418fc2e615d259b362fe",
#     "measurementId": "G-4K0SH1THBP"
# }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
# messageRef=database.ref('message')


def index(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def sendemail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        city = request.POST['city']
        msg = request.POST['msg']
        # newMessageRef=messageRef.push()
        # newMessageRef.set({
        #     name:name,
        #     email:email,
        #     phoneNumber:phoneNumber,
        #     city:city,
        #     msg:msg
        # })
        data = ContactInformation(
            name=name, email=email, phoneNumber=phoneNumber, city=city, msg=msg)
        data.save()
        send_mail("me", msg, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
    return HttpResponseRedirect("/")


def services(request):
    return render(request, 'services.html')


def intraday(request):
    return render(request, 'intraday.html')


def shortterm(request):
    return render(request, 'shortterm.html')


def mediumterm(request):
    return render(request, 'mediumterm.html')


def longterm(request):
    return render(request, 'longterm.html')


def formpage(request):
    return render(request, "formpage.html")


def formcheck(request):
    if request.method == 'POST':

        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        address = request.POST.get("address")
    
        formpage=Form(name=name,password=password,email=email,contact=contact,address=address)
        formpage.save()

    return HttpResponseRedirect("/")