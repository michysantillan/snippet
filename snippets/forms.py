from django import forms
from .models import Snippet



class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
        

class SnippetUpdateForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
        exclude = ['user']