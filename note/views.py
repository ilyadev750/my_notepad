from django.shortcuts import render, HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.
def start(request,*args, **kwargs):
    context = {}
    return render(request, 'note/first.html', context)

def note(request, *args, **kwargs):
    note = Note.objects.get(id=1)
    if request.method == 'POST':
        form = NoteForm(request.POST or None, instance=note)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            date = form.cleaned_data['date']
            form.save()
    else:
        form = NoteForm(instance=note)
    context = {}
    return render(request, 'note/editor.html', context)