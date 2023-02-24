from django.db import models
from  account.models import customUserModel #*kendi oluşturduğumuz user modelini kullanıyoruz..
from blog.models import textModel

class commentModel(models.Model):
    author = models.ForeignKey(customUserModel , on_delete=models.CASCADE, related_name ='comment')    
    text = models.ForeignKey(textModel, on_delete=models.CASCADE, related_name='commentS') 
    comment = models.TextField()
    createdAtTime = models.DateTimeField(auto_now_add=True)
    updatedAtTime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'comments'
        verbose_name ='comment'
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.author.username
    