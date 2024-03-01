from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta: 
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.name 