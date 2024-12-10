from django.shortcuts import render, redirect
from .models import Tenant


def tenants(request):
    return render(request, 'tenants/tenants.html')


def tenants_capture(request):
    if request.method == 'POST':
        name = request.POST['name']
        id_number = request.POST['id_number']
        phone_number = request.POST['phone_number']
        age = request.POST['age']
        house_number = request.POST['house_number']
        zone = request.POST['zone']

        tenant = Tenant.objects.create(name=name, id_number=id_number,phone_number=phone_number, age=age, house_number=house_number, zone=zone)
        tenant.save()

        return redirect('tenants:view')


    return render(request, 'tenants/tenants.html')

def tenants_view(request):
    all_tenants = Tenant.objects.all()
    return render(request, 'tenants/tenants.html', {'tenants': all_tenants})

def tenants_edit(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        id_number = request.POST['id_number']
        phone_number = request.POST['phone_number']
        age = request.POST['age']
        house_number = request.POST['house_number']
        zone = request.POST['zone']

        tenant = Tenant.objects.get(id=id)

        tenant.name = name
        tenant.id_number = id_number
        tenant.phone_number = phone_number
        tenant.age = age
        tenant.house_number = house_number
        tenant.zone = zone

        tenant.save()

# Create your views here.
