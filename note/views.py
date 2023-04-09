from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.template.loader import render_to_string
from .functions import prepare_data_for_form, add_info_in_object
from .models import Note
from .forms import NoteForm

# Create your views here.
def start(request,*args, **kwargs):
    context = {}
    return render(request, 'note/first.html', context)

def note(request, *args, **kwargs):
    data = prepare_data_for_form(request)
    form = NoteForm(data)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            empty_obj = Note()
            filled_odj = add_info_in_object(empty_obj, form)
            # obj.title = form.cleaned_data['title']
            # obj.content = form.cleaned_data['content']
            # obj.create = form.cleaned_data['create']
            # obj.update = form.cleaned_data['update']
            request.session['title'] = filled_odj.title
            request.session['content'] = filled_odj.content
            if request.user.is_authenticated:
                filled_odj.save()
            else:
                rendered = render_to_string('authenticate/login.html', {})
                return HttpResponse(rendered)
    context = {'form': form}
    return render(request, 'note/editor.html', context)




# реализовать создание юзеров, дать им разрешения, foreigh key изучить