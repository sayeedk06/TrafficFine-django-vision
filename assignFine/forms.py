from django import forms
from .models import Fine

class FineForm(forms.ModelForm):
    amount = forms.IntegerField(label='BDT', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Fine
        fields = ('amount',)
