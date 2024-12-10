from django.urls import path
from . import views

app_name = 'tenants'

urlpatterns = [
    path('', views.tenants, name='tenants'),
    path('tenants_captured/', views.tenants_capture, name='tenants_capture'),

    path('edit/<id>', views.tenants_edit , name='tenants_edit'),
    path('view/', views.tenants_view, name='view'),
    path('capture/', views.tenants_capture, name='tenants_capture'),
]