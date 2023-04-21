from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.files import File
from .functions import prepare_data_for_form, add_info_in_object_and_session
from .models import Note
from .forms import NoteForm

# Create your views here.
def start(request, *args, **kwargs):
    context = {}
    return render(request, 'note/first.html', context)

def note(request, *args, **kwargs):
    data = prepare_data_for_form(request)
    form = NoteForm(data)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            empty_obj = Note()
            filled_odj, request = add_info_in_object_and_session(empty_obj, form, request)
            user_actions_handler(request, filled_odj)
            # if 'save' in request.POST:
            #     filled_odj.username = request.user.username
            #     filled_odj.save()
            # elif 'download' in request.POST:
            #     pass # download note
            # elif 'register/login' in request.POST:
            #     pass # register/login
            # elif 'logout' in request.POST:
            #     pass #logout
        else:
            return render(request, 'note/first.html', {})
    context = {'form': form}
    return render(request, 'note/editor.html', context)

def user_actions_handler(request, object):
    if 'save' in request.POST:
        object.username = request.user.username
        object.save()
    elif 'download' in request.POST:
        f = open('hh.txt', 'w')
        myfile = File(f)
# сделать рефакторинг кода и прогуглить скачивание файлов



# реализовать создание юзеров, дать им разрешения, foreigh key изучить