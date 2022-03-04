from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=500)
    text = forms.CharField(max_length=250)
