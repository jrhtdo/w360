from django.db import models
from django.db import models
from django.db import models

class Donor(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    guardians_contact = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.full_name

# Create your models here.
