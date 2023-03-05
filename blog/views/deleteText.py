from django.contrib.auth.decorators import login_required
from blog.models import textModel
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class deleteTextDeleteView(DeleteView):
    template_name = 'pages/deleteTextIsOkey.html'
    success_url = reverse_lazy('mytext')
    
    def get_queryset(self):
        text = textModel.objects.filter(slug=self.kwargs['slug'], author=self.request.user)
        return text
