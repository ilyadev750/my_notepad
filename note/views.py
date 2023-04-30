
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .functions import render_to_pdf
from .functions import prepare_data_for_form, add_info_in_new_object_and_session, add_info_in_session, \
    extract_data_from_object, add_info_in_current_object_and_session
from .models import Note
from .forms import AnonymousNoteForm, UserCreateNoteForm, UserUpdateNoteForm

# Create your views here.
def start(request, *args, **kwargs):
    context = {}
    return render(request, 'note/first.html', context)

def anonymous_note(request, *args, **kwargs):
  
    data = prepare_data_for_form(request)
    form = AnonymousNoteForm(data)
    if request.method == 'POST':
        form = AnonymousNoteForm(request.POST)
        request = add_info_in_session(form, request)
        if 'register/login' in request.POST:
            return render(request, 'note/first.html', {})
        elif 'download' in request.POST:
            context = {'title': request.session['title'], 'content': request.session['content']}
            pdf = render_to_pdf('user_note.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
    context = {'form': form}
    return render(request, 'note/editor.html', context)

def get_user_notes(request, *args, **kwargs):
    if request.user.is_authenticated:
        user_objects = Note.objects.filter(username=request.user.username)
        context = {'user_objects': user_objects}
        return render(request, 'note/all_user_notes.html', context) 

def new_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        data = prepare_data_for_form(request)
        form = UserCreateNoteForm(data)
        if request.method == 'POST':
            form = UserCreateNoteForm(request.POST)
            empty_obj = Note()
            if form.is_valid():
                filled_obj, request = add_info_in_new_object_and_session(empty_obj, form, request)

                if 'save' in request.POST:
                    filled_obj.save()
                    user_id = request.user.id
                    path = f'id{user_id}/'
                    return redirect(path)


                elif 'download' in request.POST:
                    context = {'title': request.session['title'], 'content': request.session['content']}
                    pdf = render_to_pdf('user_note.html', context)
                    return HttpResponse(pdf, content_type='application/pdf')
                

                elif 'logout' in request.POST:
                    return render(request, 'note/first.html', {})
        context = {'form': form }
        return render(request, 'note/editor.html', context)    
    
def update_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        title = request.path.split('/')
        title = title[-2]
        current_user_object = Note.objects.get(username=request.user.username, title=title)
        data = extract_data_from_object(current_user_object)
        form = UserUpdateNoteForm(data)
        if request.method == 'POST':
            form = UserUpdateNoteForm(request.POST)
            if form.is_valid():
                current_user_object, request = add_info_in_current_object_and_session(current_user_object, form,
                                                                                      request)

            if 'save' in request.POST:
                current_user_object.save()
                user_id = request.user.id
                path = f"http://127.0.0.1:8000/base/users/id{user_id}/"
                return redirect(path)
            
            elif 'download' in request.POST:
                context = {'title': request.session['title'], 'content': request.session['content']}
                pdf = render_to_pdf('user_note.html', context)
                return HttpResponse(pdf, content_type='application/pdf')
            
            elif 'logout' in request.POST:
                return render(request, 'note/first.html', {})

        context = {'form': form}
        return render(request, 'note/editor.html', context)


# сделать отдельные отображения как для аноноимной формы, так и для зарегистрированного
#  пользователя, сделать маршрутизацию и отображение заметок по каждому пользователю с 
# возможностью менять заметки



# реализовать создание юзеров, дать им разрешения, foreigh key изучить