from django.contrib import admin
from blog.models import categoryModel
from blog.models import textModel
from blog.models import commentModel
from blog.models import contactModel

# Register your models here.

admin.site.register(categoryModel)


# Admini customize etmek için :
class textAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content') #
    list_display = ('title', 'createdAtTime','updatedAtTime')
admin.site.register(textModel, textAdmin) #parametre olarak textAdmini eklemeliyiz.

class commentAdmin(admin.ModelAdmin):
    search_fields= ('author__username',)
    list_display = ('comment', 'createdAtTime', 'updatedAtTime')
admin.site.register(commentModel, commentAdmin)

class contactAdmin(admin.ModelAdmin):
    search_fields = ('email')
    list_display = ('email','createdAtTime')

admin.site.register(contactModel)
