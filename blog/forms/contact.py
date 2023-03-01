from django import forms


class contactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name_lastname = forms.CharField(max_length=30)
    message = forms.CharField(widget = forms.Textarea)