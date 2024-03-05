from rest_framework.viewsets import ModelViewSet
from .serializers import ContactsSerializer
from ..models import Contacts

class CreateContactsViewSet(ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
