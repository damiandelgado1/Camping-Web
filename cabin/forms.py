from django import forms

class SearchCabin(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))