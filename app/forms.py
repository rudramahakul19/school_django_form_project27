from django import forms


class Schoolform(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()

