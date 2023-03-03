from django.urls import path
from .views import out ,changePassword,changeProfil


urlpatterns = [
    path ('out',out,name='out'),
    path('change-password', changePassword, name='change-password'),
    path('change-profil', changeProfil, name= 'change-profil'),
]
