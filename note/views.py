
import os
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.views import logout
from .functions import render_to_pdf
from .functions import prepare_data_for_form, add_info_in_new_object_and_session, add_info_in_session, \
    extract_data_from_object, add_info_in_current_object_and_session
from .forms import AnonymousNoteForm, UserCreateNoteForm, UserUpdateNoteForm
from .models import Note

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
        context = {'user_objects': user_objects, 'user_id': request.user.id}
        return render(request, 'note/all_user_notes.html', context) 

def new_user_note(request, *args, **kwargs):
    if kwargs['type_of_note'] == 'new':
        request.session['title'] = ''
        request.session['content'] = ''
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
                    return redirect('get_user_notes', request.user.id)

                elif 'download' in request.POST:
                    context = {'title': request.session['title'], 'content': request.session['content']}
                    pdf = render_to_pdf('user_note.html', context)
                    return HttpResponse(pdf, content_type='application/pdf')
                
                elif 'logout' in request.POST:
                    logout(request)
                    return redirect('start')
        context = {'form': form, 'fields': ['title', 'content'] }
        return render(request, 'note/editor.html', context)

def delete_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        title = kwargs['title']
        id = kwargs['id']
        current_user_object = Note.objects.get(id=id, title=title)
        current_user_object.delete()
        return redirect('get_user_notes', request.user.id)
    
def update_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        title = kwargs['title']
        id = kwargs['id']
        current_user_object = Note.objects.get(id=id, title=title)
        data = extract_data_from_object(current_user_object)
        form = UserUpdateNoteForm(data)
        if request.method == 'POST':
            form = UserUpdateNoteForm(request.POST)
            if form.is_valid():
                current_user_object, request = add_info_in_current_object_and_session(current_user_object, form,
                                                                                      request)

            if 'save' in request.POST:
                current_user_object.save()
                return redirect('get_user_notes', request.user.id)
            
            elif 'download' in request.POST:
                context = {'title': request.session['title'], 'content': request.session['content']}
                pdf = render_to_pdf('user_note.html', context)
                return HttpResponse(pdf, content_type='application/pdf')
            
            elif 'logout' in request.POST:
                logout(request)
                return redirect('start')

        context = {'form': form}
        return render(request, 'note/editor.html', context)


# сделать отдельные отображения как для аноноимной формы, так и для зарегистрированного
#  пользователя, сделать маршрутизацию и отображение заметок по каждому пользователю с 
# возможностью менять заметки



# реализовать создание юзеров, дать им разрешения, foreigh key изучить