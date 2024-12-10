from django.urls import path
from visitors import views

app_name = 'visitors'

urlpatterns = [
    path('visitors/', views.visitors, name='visitors'),
    path('visitors_captured/', views.visitors_capture, name= 'visitors_captured'),

    path('edit/<id>', views.visitors_edit, name='visitors_edit'),
    path('show/', views.visitors_view )
]