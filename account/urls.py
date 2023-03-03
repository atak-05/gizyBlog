from django.urls import path
from .views import out ,changePassword


urlpatterns = [
    path ('out',out,name='out'),
    path('change-password', changePassword, name='change-password'),
]
