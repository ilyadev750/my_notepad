from .models import Note
from django import forms
from django.utils import timezone

class NoteForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "new class",
        "placeholder": "description",
        "rows": 10,
        "cols": 10
    }))
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())

