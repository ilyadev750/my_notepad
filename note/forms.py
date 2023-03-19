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
        fields = '__all__'