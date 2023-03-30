from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Note
from .forms import NoteForm

# Create your views here.
def start(request,*args, **kwargs):
    context = {}
    return render(request, 'note/editor.html', context)

def note(request, *args, **kwargs):
    data = {'title': '', 
            'content': '', 
            'create': timezone.now(), 
            'update': timezone.now()}
    form = NoteForm(data)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = Note()
            obj.title = form.cleaned_data['title']
            obj.content = form.cleaned_data['content']
            obj.create = form.cleaned_data['create']
            obj.update = form.cleaned_data['update']
            obj.save()
    context = {'form': form}
    return render(request, 'note/editor.html', context)

# реализовать создание юзеров, дать им разрешения, foreigh key изучить