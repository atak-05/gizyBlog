from django import forms
from blog.models import commentModel

class commentAddForm(forms.ModelForm):
    class Meta:
        model = commentModel
        fields = ('comment',)