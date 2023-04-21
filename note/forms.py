from .models import Note
from django import forms
from django.utils import timezone

class NoteForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "note-content",
        "placeholder": "",
        "name": "content",
        "rows": 10,
        "cols": 10,
    }), required=False)
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())

# class UserForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)

