from django.contrib.auth.decorators import login_required
from blog.models import textModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def deleteText(request,slug):
    get_object_or_404(textModel, slug=slug , author = request.user).delete()
    return redirect('mytext')