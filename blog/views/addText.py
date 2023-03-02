from django.shortcuts import render, redirect
from blog.forms import textAddForm
from django.contrib.auth.decorators import login_required

# m2m datası farklı bir yerde olduğu için onuda 
# -bu şekilde kayıt ediyoruz.
@login_required(login_url='/')
def addText(request):
    form = textAddForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        text = form.save(commit=False)
        text.author = request.user
        text.save()       
        form.save_m2m() 
        return redirect('detail', slug= text.slug)
    return render(request, 'pages/addText.html', context={
        'form': form
    })

