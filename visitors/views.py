from django.shortcuts import render, redirect
from .models import Visitor


def visitors(request):
    return render(request, 'visitors/visitors.html')


def visitors_capture(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        id_number = request.POST['id_number']
        vehicle_number = request.POST['vehicle_number']
        vehicle_model = request.POST['vehicle_model']

        visitor = Visitor(name=name, phone_number=phone_number, id_number=id_number,vehicle_number=vehicle_number,vehicle_model=vehicle_model)
        visitor.save()

        return visitors_view(request)


def visitors_view(request):
    all_visitors = Visitor.objects.all()
    return render(request, 'visitors/visitors.html', {'visitors': all_visitors})


def visitors_edit(request, id):

    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        id_number = request.POST['id_number']
        vehicle_number = request.POST['vehicle_number']
        vehicle_model = request.POST['vehicle_model']

    visitor = Visitor.objects.get(id=id)

    visitor.name = name
    visitor.phone_number = phone_number
    visitor.id_number = id_number
    visitor.vehicle_number = vehicle_number
    visitor.vehicle_model = vehicle_model

    visitor.save()
# Create your views here.
