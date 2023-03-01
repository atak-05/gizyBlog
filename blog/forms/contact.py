from django import forms
from blog.models import contactModel

class contactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = ('name_lastname', 'email','message')
        