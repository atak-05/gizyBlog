from django.urls import path
from blog.views import (contact,
                        home,
                        category,
                        mytext)

# * config/urls içerisinden gelen istediğin cevabı burada blog için
urlpatterns = [
    path('', home, name='home'),
    path('contact' , contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('mytext', mytext, name='mytext'),
]
    
