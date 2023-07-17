# forms.py
from django import forms
from .models import DiaryEntry

class DiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title']

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title', 'content']
