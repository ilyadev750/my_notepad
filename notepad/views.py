from django.shortcuts import render

from .models import Notepad

def index(request):
    note = Notepad.objects.get(id=1)
    return render(request, 'notepad_templates/index.html', {note: 'note'})
