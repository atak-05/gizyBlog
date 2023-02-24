from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import customUserModel
# Register your models here.


class customAdmin(UserAdmin):
    model = customUserModel
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı', {
            'fields': ['avatar']
        }),
    ) #*burada yaptıgımız işlem useradmin içindeki fieldsetleri kullandık ve artı olarak avatar alanımızı oluşturduk!


admin.site.register(customUserModel, customAdmin)
