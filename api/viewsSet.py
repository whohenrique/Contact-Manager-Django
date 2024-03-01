from django.shortcuts import render
from .serializers import ContactsSerializer
from .models import Contacts
from rest_framework import viewsets

class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()