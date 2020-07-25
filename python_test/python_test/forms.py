# view form models
from django.forms import ModelForm, Form, EmailField, HiddenInput, CharField, ChoiceField
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

ORDER_FIELD_CHOICES =( 
    ("client_name", "Client Name"), 
    ("email", "Email Address"), 
    ("phone_number", "Phone Number"), 
    ("suburb", "Suburb") 
) 

ORDER_TYPE_CHOICES =( 
    ("", "ASC"), 
    ("-", "DESC")
) 

class ClientSearchForm(Form):
    client_name = CharField(label="Client Name", max_length=50, required=False)
    email = EmailField(label="Email Address", max_length=50, required=False)
    phone_number = CharField(label="Phone Number", max_length=50, required=False)
    suburb = CharField(label="Suburb", max_length=80, required=False)
    order_by = ChoiceField(label="Order By", choices=ORDER_FIELD_CHOICES, required=False)
    order_type = ChoiceField(label="Order Type", choices=ORDER_TYPE_CHOICES, required=False)



