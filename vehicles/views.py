from django.shortcuts import render, redirect
from .models import Vehicle
def vehicles(request):
    return render(request, 'vehicles/vehicles.html')

def vehicles_capture(request):
    if request.method == "POST":
        name = request.POST['name']
        registration_number = request.POST['registration_number']
        model= request.POST['model']
        make= request.POST['make']

        vehicle = Vehicle(name=name,registration_number=registration_number,model=model,make=make)
        vehicle.save()

        return redirect('vehicles:vehicles_view')


    return render(request, 'vehicles/vehicles.html')

def vehicles_view(request):
    all_vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicles.html', {'vehicles': all_vehicles})

def vehicles_edit(request, id):

    if request.method == "POST":
        name = request.POST['name']
        registration_number = request.POST['registration_number']
        model = request.POST['model']
        make = request.POST['make']

    vehicle = Vehicle.objects.get(id=id)

    vehicle.name = name
    vehicle.registration_number = registration_number
    vehicle.model = model
    vehicle.make = make

    vehicle.save()

# Create your views here.
