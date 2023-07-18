from django import forms

class SignUpForm(forms.Form):

    g=[('male','MALE'),('female','FEMALE')]

    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=g)