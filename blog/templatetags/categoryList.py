from blog.models import categoryModel
from django import template

#template taglarını ve filterlerini kaydetmek için kullanılır.
register = template.Library()

@register.simple_tag
def categoryList():
    categories = categoryModel.objects.all()
    return categories