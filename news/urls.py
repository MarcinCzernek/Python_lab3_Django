from django.urls import path, include
from .views import index, add, get, editnews, updatenews, displaydata

urlpatterns = [
    path('', index, name="view_news"),
    path('add/', add, name="add"),
    path('editnews/', displaydata, name="displaydata"),
    path('edit/<int:id>', editnews),
    path('update/<int:id>', updatenews),
    path('home/', include('home.urls')),
    path('<int:id>/', get, name='get'),
]
