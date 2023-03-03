from django.urls import path
from .views.out import out


urlpatterns = [
    path ('out',out,name='out')
]
