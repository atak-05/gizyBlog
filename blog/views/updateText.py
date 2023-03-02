from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import textUpdateForm
from blog.models import textModel
from django.contrib.auth.decorators import login_required

# m2m datası farklı bir yerde olduğu için onuda 
# -bu şekilde kayıt ediyoruz.
@login_required(login_url='/')
def updateText(request,slug):
    text = get_object_or_404(textModel, slug=slug, author= request.user)
    form = textUpdateForm(request.POST or None, files=request.FILES or None,
            instance=text)
    if form.is_valid():
        form.save()
        return redirect('detail', slug = text.slug)
    return render(request, 'pages/updateText.html', context={
        'form': form,
    })