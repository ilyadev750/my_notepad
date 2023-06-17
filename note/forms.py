from .models import Note
from django import forms
from django.utils import timezone


class AnonymousNoteForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-content-title"}),
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-content"}),
        required=False,
    )
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())


class UserCreateNoteForm(forms.Form):
    title = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={"class": "editor-container"})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "editor-container"})
    )
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())


class UserUpdateNoteForm(forms.Form):
    title = forms.CharField(max_length=255, error_messages={"required": ""})
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "note-content",
                "placeholder": "",
                "name": "content",
                "rows": 10,
                "cols": 10,
            }
        ),
        error_messages={"required": ""},
    )
    update = forms.DateTimeField(widget=forms.HiddenInput())
