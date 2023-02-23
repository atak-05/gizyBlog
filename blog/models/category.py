from django.db import models
from autoslug import AutoSlugField

class categoryModel(models.Model):
    categoryName = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='categoryName', unique = True)
    class Meta:
        db_table = 'category' #tablonun adı
        verbose_name_plural = 'Categories' #panelledeki kategori ismini düzenledik.
        verbose_name = 'category' #üst taraftaki yazıyı düzenledik.
        
    def __str__(self):
        return self.categoryName #category isimlerini döndürüyor.