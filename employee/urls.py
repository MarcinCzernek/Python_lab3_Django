from django.contrib import admin
from django.urls import path, include
from . import views
from .views import addemp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.displaydata, name="displaydata"),
    path('employee/edit/<int:id>',views.editemp),
    path('employee/update/<int:id>',views.updateemp),
    path('delete/<int:id>',views.deleteemp),
    path('employee/add/', addemp, name="add"),
    path('home/', include('home.urls')),
]