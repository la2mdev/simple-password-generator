from django.urls import path
from .views import index, get_password


app_name = 'generator'
urlpatterns = [
    path('', index, name='index'),
    path('get_password/', get_password, name='get_password')
]
