from django.shortcuts import render, get_object_or_404
from blog.models import textModel

def detail(request,slug):
    text = get_object_or_404(textModel, slug=slug)
    print(text)
    comments = text.commentS.all()
    return render(request,'pages/detail.html', context={
        'text': text,
        'comments': comments
    })
    
    
