from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles_captured/', views.vehicles_capture, name='vehicles_capture'),

    path('edit/<id>/', views.vehicles_edit, name='vehicles_edit'),
    path('vehicles_view/', views.vehicles_view, name='vehicles_view'),
]