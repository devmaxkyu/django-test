# Insert models here
from django.db import models

class Address(models.Model):
    street = models.CharField(
        "Street Address", 
        max_length=80
    )
    suburb = models.CharField(
        "Suburb Address", 
        max_length=80
    )
    postalcode = models.CharField(
        "ZIP / Postal code", 
        max_length=12
    )
    state = models.CharField(
        "State Name", 
        max_length=50
    )

    class Meta:
        indexes = [
            models.Index(fields=['suburb'], name='suburb_idx')
        ]    

class Client(models.Model):    
    client_name = models.CharField(
        "Last Name", 
        max_length=50, 
        null=True, 
        unique=True  # Unique Constraints
    )
    contact_name = models.CharField(
        "Contact Name", 
        max_length=50, 
        null=True
    )
    email = models.CharField(
        "Email", 
        max_length=50,
        unique=True  # Unique Constraints
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True
    )
    phone_number = models.CharField(
        "Phone Number", 
        max_length=50
    )
