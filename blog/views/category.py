from django.shortcuts import render, get_object_or_404
from blog.models import textModel
from django.core.paginator import Paginator
from blog.models import categoryModel

#* urlsden gelen istediğin cevabı bu sayfada 

#* __init__.py sayfasına dahil etmeyi unutma!

def category(request,categorySlug):
    category = get_object_or_404(categoryModel, slug=categorySlug)
    texts = category.text.order_by('-id') #ters ilişki text model içerisindeki M2M sayesinde yaptık. #
    page = request.GET.get('page')
    paginator = Paginator(texts, 1)
    return render(request , 'pages/category.html', context={
        'texts': paginator.get_page(page),
        'categoryName': category.categoryName
        
    })
    


