from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    print(name)
    file  = forms.FileField()
    print(file)