from django.shortcuts import render



#* __init__.py sayfasına dahil etmeyi unutma!
def contact(request):
    return render(request , 'pages/contact.html', context={})