
from django.contrib import admin
from .models import ContactInformation
from .models import Form
# Register your models here.
@admin.register(ContactInformation)
class UserAdmin(admin.ModelAdmin):
    list_display=("name","email","phoneNumber","city","msg")

@admin.register(Form)
class Form(admin.ModelAdmin):
    list_display=("name","password","email","contact","address")