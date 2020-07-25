from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from python_test.forms import ClientCreateForm, ClientUpdateForm, AddressForm
from python_test.models import Client

# Insert views here

def index(request):
    clients = Client.objects.all()
    return render(request, 'clients/index.html', {'clients': clients})

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required            
            client = form.save()
            # redirect to a detail page:
            return redirect('client_detail', client_id=client.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientCreateForm()

    return render(request, 'clients/create.html', {'form': form})

def update(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        renew_client = {
            "client_name": request.POST['client_name'],
            "contact_name": request.POST['contact_name'],
            "email": request.POST['email'],
            "phone_number": request.POST['phone_number'],
            "address": request.POST['address']
        }

        form = ClientUpdateForm(request.POST, instance=client)

        if client.address:
            address_form = AddressForm(request.POST, instance=client.address)
        else:
            address_form = AddressForm(request.POST)

        # Check if the form is valid:
        if form.is_valid() and address_form.is_valid():
            address = address_form.save()
            client.address = address
            client = form.save()
            # redirect to a detail page:
            return redirect('client_detail', client_id=client.id)
    else:
        form = ClientUpdateForm(instance=client)

        if client.address:
            address_form = AddressForm(instance=client.address)
        else:
            address_form = AddressForm()

    context = {
        'form': form,
        'address_form': address_form,
        'client_id': client_id
    }
    
    return render(request, 'clients/update.html', context)

def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clients/detail.html', {'client': client})