from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=500, widget=forms.Textarea())
    text = forms.CharField(max_length=250, widget=forms.Textarea())
#     files = forms.FileField() #you can also attach a file 
