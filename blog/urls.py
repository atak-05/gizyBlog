from django.urls import path
from blog.views import (contact,
                        home,
                        category,
                        mytext,
                        detail,
                        addText,
                        updateText,
                        deleteText,
                        deleteComment
                        )
from django.views.generic import TemplateView

# * config/urls içerisinden gelen istediğin cevabı burada blog için
urlpatterns = [
    path('', home, name='home'),
    path('about', TemplateView.as_view(
        template_name='pages/about.html'
        ) , name='about'),
    path('contact' , contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('mytext', mytext, name='mytext'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-text',addText, name='addText'),
    path('update-text/<slug:slug>', updateText, name='update-text'),
    path('delete-text/<slug:slug>', deleteText, name='delete-text'),
    path('delete-comment/<int:id>', deleteComment, name='delete-comment'),

]
    
