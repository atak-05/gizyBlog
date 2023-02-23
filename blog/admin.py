from django.contrib import admin
from blog.models import categoryModel
from blog.models import textModel

# Register your models here.

admin.site.register(categoryModel)


# Admini customize etmek için :
class textAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content') #
    list_display = ('title', 'createdAtTime','updatedAtTime')
admin.site.register(textModel, textAdmin) #parametre olarak textAdmini eklemeliyiz.

