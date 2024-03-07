from django import forms
from ckeditor.widgets import CKEditorWidget


class AnonymousNoteForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-content-title"}),
    )
    content = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
    )
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())


class UserCreateNoteForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-content-title"})
    )
    content = forms.CharField(widget=CKEditorWidget())
    create = forms.DateTimeField(widget=forms.HiddenInput())
    update = forms.DateTimeField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())


class UserUpdateNoteForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        error_messages={"required": ""},
        widget=forms.TextInput(attrs={"class": "form-content-title"}),
    )
    content = forms.CharField(
        widget=CKEditorWidget(),
        error_messages={"required": ""},
    )
    update = forms.DateTimeField(widget=forms.HiddenInput())
