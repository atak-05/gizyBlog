from django.urls import path
from blog.views import (contact,
                        home,)

# * config/urls içerisinden gelen istediğin cevabı burada blog için
urlpatterns = [
    path('', home),
    path('contact' , contact),
]
    
