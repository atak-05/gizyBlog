from django.shortcuts import render, get_object_or_404
from blog.models import textModel
from blog.forms import commentAddForm
def detail(request,slug):
    text = get_object_or_404(textModel, slug=slug)
    print(text)
    comments = text.commentS.all()
    
    if request.method == 'POST':
        addComment = commentAddForm(data=request.POST)
        if addComment.is_valid():
            comment = addComment.save(commit=False)
            comment.author =request.user
            comment.text = text
            comment.save()       
        
    addComment = commentAddForm()
    
    
    return render(request,'pages/detail.html', context={
        'text': text,
        'comments': comments,
        'addComment': addComment,
    })
    
    
