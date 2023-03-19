from .models import Note
from django import forms

class NoteForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "new class",
        "placeholder": "description",
        "rows": 10,
        "cols": 10
    }))
    class Meta:
        model = Note
        fields = ['title', 'content', 'create', 'update']
        # widgets = {'create': forms.HiddenInput,
        #            'update': forms.HiddenInput,}