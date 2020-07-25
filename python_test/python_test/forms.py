# view form models
from django.forms import ModelForm, EmailField, HiddenInput
from python_test.models import Address, Client

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'suburb', 'postal_code', 'state']

class ClientCreateForm(ModelForm):
    email = EmailField()
    class Meta:
        model = Client
        fields = ['client_name', 'email', 'phone_number']

class ClientUpdateForm(ModelForm):
    email = EmailField()
    class Meta:
        model = Client
        fields = ['client_name', 'contact_name', 'email', 'phone_number', 'address']
        widgets = {'address': HiddenInput()}


