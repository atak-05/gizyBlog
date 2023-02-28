from django.shortcuts import render, get_object_or_404
from blog.models import textModel, commentModel

def detail(request,slug):
    text = get_object_or_404(textModel, slug=slug)
    print(text)
    comment = text.commentS.all()
    return render(request,'pages/detail.html', context={
        'text': text,
        'comment': comment
    })