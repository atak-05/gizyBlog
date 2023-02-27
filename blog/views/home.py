from django.shortcuts import render
from blog.models import textModel
#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!

def home(request):
    texts = textModel.objects.all()
    return render(request , 'pages/home.html', context={
        'texts': texts
    })


