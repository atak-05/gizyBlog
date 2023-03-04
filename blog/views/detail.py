from django.shortcuts import render, get_object_or_404, redirect
from blog.models import textModel
from blog.forms import commentAddForm
from django.views import View
from django.contrib import messages


class detailView(View):
    http_method_names= ['get', 'post']
    commentAddForm_ = commentAddForm
    
    def get(self, request,slug):
        text = get_object_or_404(textModel, slug=slug)
        comments = text.commentS.all()
        return render(request,'pages/detail.html', context={
        'text': text,
        'comments': comments,
        'addComment': self.commentAddForm_,
    })
        
    def post(self, request,slug):
        text = get_object_or_404(textModel, slug=slug)
        commentAddForm_ = self.commentAddForm_(data=request.POST)
        if commentAddForm_.is_valid():
            comment = commentAddForm_.save(commit=False)
            comment.author =request.user
            comment.text = text
            comment.save()   
            messages.success(request, "Comment added successfully")
        return redirect('detail', slug=slug)
 


    
