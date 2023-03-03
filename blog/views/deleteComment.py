from django.contrib.auth.decorators import login_required
from blog.models import commentModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def deleteComment(request,id):
    comment =  get_object_or_404(commentModel, id=id)
    if comment.author == request.user or comment.text.author == request.user:
        comment.delete()
        return redirect('detail', slug= comment.text.slug)
    return redirect('home')