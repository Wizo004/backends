from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('', views.payments, name='payments'),


    path('edit/<int:id>', views.payment_edit, name='payment_edit'),
    path('view_payments/', views.payment_fetch, name='payment_view'),
]