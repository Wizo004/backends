"""
URL configuration for estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.index, name='index')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='index')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import tenants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('payments/', include('payments.urls')),
    path('tenants/', include('tenants.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('visitors/', include('visitors.urls')),




]
