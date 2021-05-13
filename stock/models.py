from django.db import models

# Create your models here.
class ContactInformation(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneNumber= models.CharField(max_length=15)
    city=models.CharField(max_length=25)
    msg=models.CharField(max_length=500)

