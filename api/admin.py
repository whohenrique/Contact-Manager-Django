from django.contrib import admin
from .models import Contacts

# Register your models here.

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')