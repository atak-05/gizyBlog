from django.urls import path
from .views import out ,changePassword,changeProfil,signIn
from django.contrib.auth import views as auth_views


#as_view ile örnegin LoginView içindeki overrides edebiliyorz.
urlpatterns = [
    path('login',auth_views.LoginView.as_view(
        template_name='pages/login.html'
        ), name='login' ),
    
    path ('out',out,name='out'),
    
    path('change-password', changePassword, name='change-password'),
    
    path('change-profil', changeProfil, name= 'change-profil'),
    
    path('sign-in', signIn, name= 'sign-in'),

]
