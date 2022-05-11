"""Python_lab3_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from news.views import displaydata, editnews, updatenews
from employee.views import editemp,updateemp,deleteemp,addemp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('news/', include('news.urls')),
    path('', include('authentication.urls')),
    path('editnews/', displaydata, name="displaydata"),
    path('edit/<int:id>',editnews),
    path('update/<int:id>',updatenews),
    path('employee/', include('employee.urls')),
    path('employee/edit/<int:id>', editemp),
    path('employee/update/<int:id>', updateemp),
    path('delete/<int:id>', deleteemp),
    path('employee/add/', addemp, name="add"),

]
