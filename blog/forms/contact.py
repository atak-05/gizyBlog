from django import forms


class contactForm(forms.Form):
    email = forms.EmailField(label= 'E-mail', max_length=100)
    name_lastname = forms.CharField(label='Name Lastname',max_length=30)
    message = forms.CharField(label='Your Message' ,widget = forms.Textarea) #widgetlar <htmltaglaridir>