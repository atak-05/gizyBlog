from django.shortcuts import render

#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!

def home(request):
    return render(request , 'pages/home.html', context={})


