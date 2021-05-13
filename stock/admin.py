
from django.contrib import admin
from .models import ContactInformation
# Register your models here.
@admin.register(ContactInformation)
class UserAdmin(admin.ModelAdmin):
    list_display=("name","email","phoneNumber","city","msg")
