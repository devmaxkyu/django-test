# db models
from django.db import models

class Address(models.Model):
    street = models.CharField(
        "Street Address", 
        max_length=80,
        null=True,
        blank=True
    )
    suburb = models.CharField(
        "Suburb Address", 
        max_length=80,
        null=True,
        blank=True
    )
    postal_code = models.CharField(
        "ZIP / Postal code", 
        max_length=12,
        null=True,
        blank=True
    )
    state = models.CharField(
        "State Name", 
        max_length=50,
        null=True,
        blank=True
    )

    @property
    def full_address(self):
        full_address = []

        if self.street:
            full_address.append(self.street)
        if self.suburb:
            full_address.append(self.suburb)
        if self.postal_code:
            full_address.append(self.postal_code)
        if self.state:
            full_address.append(self.state)

        return ', '.join(full_address)

    class Meta:
        indexes = [
            models.Index(fields=['suburb'], name='suburb_idx')
        ]    

class Client(models.Model):    
    client_name = models.CharField(
        "Client Name", 
        max_length=50,
        unique=True  # Unique Constraints
    )
    contact_name = models.CharField(
        "Contact Name", 
        max_length=50, 
        null=True,
        blank=True
    )
    email = models.CharField(
        "Email", 
        max_length=50,
        unique=True  # Unique Constraints
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        "Phone Number", 
        max_length=50
    )


