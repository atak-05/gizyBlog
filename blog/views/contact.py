from django.shortcuts import render, redirect
from blog.forms import contactForm
from blog.models import contactModel

#* __init__.py sayfasına dahil etmeyi unutma!
def contact(request):
    form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST)
        print(form)
        if form.is_valid():
            contact = contactModel()
            contact.email = form.cleaned_data['email']
            contact.name_lastname = form.cleaned_data['name_lastname']
            contact.message = form.cleaned_data['message']
            contact.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request , 'pages/contact.html', context = context)

